# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
import threading
from bstack_utils.helper import bstack11l11l111l_opy_
from bstack_utils.constants import bstack11l1l1111ll_opy_, EVENTS, STAGE
from bstack_utils.bstack1ll11111l1_opy_ import get_logger
logger = get_logger(__name__)
class bstack1llll111_opy_:
    bstack11l11ll1111_opy_ = None
    @classmethod
    def bstack111l1l1l1_opy_(cls):
        if cls.on() and os.getenv(bstack1lllll1_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠤ᫥")):
            logger.info(
                bstack1lllll1_opy_ (u"ࠬ࡜ࡩࡴ࡫ࡷࠤ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽࠡࡶࡲࠤࡻ࡯ࡥࡸࠢࡥࡹ࡮ࡲࡤࠡࡴࡨࡴࡴࡸࡴ࠭ࠢ࡬ࡲࡸ࡯ࡧࡩࡶࡶ࠰ࠥࡧ࡮ࡥࠢࡰࡥࡳࡿࠠ࡮ࡱࡵࡩࠥࡪࡥࡣࡷࡪ࡫࡮ࡴࡧࠡ࡫ࡱࡪࡴࡸ࡭ࡢࡶ࡬ࡳࡳࠦࡡ࡭࡮ࠣࡥࡹࠦ࡯࡯ࡧࠣࡴࡱࡧࡣࡦࠣ࡟ࡲࠬ᫦").format(os.getenv(bstack1lllll1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠦ᫧"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ᫨"), None) is None or os.environ[bstack1lllll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ᫩")] == bstack1lllll1_opy_ (u"ࠤࡱࡹࡱࡲࠢ᫪"):
            return False
        return True
    @classmethod
    def bstack11l11l1l11l_opy_(cls, bs_config, framework=bstack1lllll1_opy_ (u"ࠥࠦ᫫")):
        bstack11ll1l11ll1_opy_ = False
        for fw in bstack11l1l1111ll_opy_:
            if fw in framework:
                bstack11ll1l11ll1_opy_ = True
        return bstack11l11l111l_opy_(bs_config.get(bstack1lllll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ᫬"), bstack11ll1l11ll1_opy_))
    @classmethod
    def bstack11l11l1ll11_opy_(cls, framework):
        return framework in bstack11l1l1111ll_opy_
    @classmethod
    def bstack11l11l1ll1l_opy_(cls, bs_config, framework):
        return cls.bstack11l11l1l11l_opy_(bs_config, framework) is True and cls.bstack11l11l1ll11_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack1lllll1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ᫭"), None)
    @staticmethod
    def bstack1l1l11ll_opy_():
        if getattr(threading.current_thread(), bstack1lllll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪ᫮"), None):
            return {
                bstack1lllll1_opy_ (u"ࠧࡵࡻࡳࡩࠬ᫯"): bstack1lllll1_opy_ (u"ࠨࡶࡨࡷࡹ࠭᫰"),
                bstack1lllll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ᫱"): getattr(threading.current_thread(), bstack1lllll1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧ᫲"), None)
            }
        if getattr(threading.current_thread(), bstack1lllll1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨ᫳"), None):
            return {
                bstack1lllll1_opy_ (u"ࠬࡺࡹࡱࡧࠪ᫴"): bstack1lllll1_opy_ (u"࠭ࡨࡰࡱ࡮ࠫ᫵"),
                bstack1lllll1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ᫶"): getattr(threading.current_thread(), bstack1lllll1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬ᫷"), None)
            }
        return None
    @staticmethod
    def bstack11l11l1l1l1_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1llll111_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1l111l1l_opy_(test, hook_name=None):
        bstack11l11l1l1ll_opy_ = test.parent
        if hook_name in [bstack1lllll1_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧ᫸"), bstack1lllll1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫ᫹"), bstack1lllll1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠪ᫺"), bstack1lllll1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠧ᫻")]:
            bstack11l11l1l1ll_opy_ = test
        scope = []
        while bstack11l11l1l1ll_opy_ is not None:
            scope.append(bstack11l11l1l1ll_opy_.name)
            bstack11l11l1l1ll_opy_ = bstack11l11l1l1ll_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11l11l1llll_opy_(hook_type):
        if hook_type == bstack1lllll1_opy_ (u"ࠨࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠦ᫼"):
            return bstack1lllll1_opy_ (u"ࠢࡔࡧࡷࡹࡵࠦࡨࡰࡱ࡮ࠦ᫽")
        elif hook_type == bstack1lllll1_opy_ (u"ࠣࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠧ᫾"):
            return bstack1lllll1_opy_ (u"ࠤࡗࡩࡦࡸࡤࡰࡹࡱࠤ࡭ࡵ࡯࡬ࠤ᫿")
    @staticmethod
    def bstack11l11l1lll1_opy_(bstack111111ll_opy_):
        try:
            if not bstack1llll111_opy_.on():
                return bstack111111ll_opy_
            if os.environ.get(bstack1lllll1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠣᬀ"), None) == bstack1lllll1_opy_ (u"ࠦࡹࡸࡵࡦࠤᬁ"):
                tests = os.environ.get(bstack1lllll1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࡢࡘࡊ࡙ࡔࡔࠤᬂ"), None)
                if tests is None or tests == bstack1lllll1_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦᬃ"):
                    return bstack111111ll_opy_
                bstack111111ll_opy_ = tests.split(bstack1lllll1_opy_ (u"ࠧ࠭ࠩᬄ"))
                return bstack111111ll_opy_
        except Exception as exc:
            logger.debug(bstack1lllll1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡳࡧࡵࡹࡳࠦࡨࡢࡰࡧࡰࡪࡸ࠺ࠡࠤᬅ") + str(str(exc)) + bstack1lllll1_opy_ (u"ࠤࠥᬆ"))
        return bstack111111ll_opy_