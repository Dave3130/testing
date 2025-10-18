# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import os
import threading
from bstack_utils.helper import bstack111ll11ll_opy_
from bstack_utils.constants import bstack11l1l111ll1_opy_, EVENTS, STAGE
from bstack_utils.bstack111l11l1l_opy_ import get_logger
logger = get_logger(__name__)
class bstack1l11lll1_opy_:
    bstack11l11l1l111_opy_ = None
    @classmethod
    def bstack1ll1l1l1ll_opy_(cls):
        if cls.on() and os.getenv(bstack1l1lll1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠦ᫠")):
            logger.info(
                bstack1l1lll1_opy_ (u"ࠧࡗ࡫ࡶ࡭ࡹࠦࡨࡵࡶࡳࡷ࠿࠵࠯ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿࠣࡸࡴࠦࡶࡪࡧࡺࠤࡧࡻࡩ࡭ࡦࠣࡶࡪࡶ࡯ࡳࡶ࠯ࠤ࡮ࡴࡳࡪࡩ࡫ࡸࡸ࠲ࠠࡢࡰࡧࠤࡲࡧ࡮ࡺࠢࡰࡳࡷ࡫ࠠࡥࡧࡥࡹ࡬࡭ࡩ࡯ࡩࠣ࡭ࡳ࡬࡯ࡳ࡯ࡤࡸ࡮ࡵ࡮ࠡࡣ࡯ࡰࠥࡧࡴࠡࡱࡱࡩࠥࡶ࡬ࡢࡥࡨࠥࡡࡴࠧ᫡").format(os.getenv(bstack1l1lll1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉࠨ᫢"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack1l1lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭᫣"), None) is None or os.environ[bstack1l1lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ᫤")] == bstack1l1lll1_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ᫥"):
            return False
        return True
    @classmethod
    def bstack11l11l1l11l_opy_(cls, bs_config, framework=bstack1l1lll1_opy_ (u"ࠧࠨ᫦")):
        bstack11ll1l11l1l_opy_ = False
        for fw in bstack11l1l111ll1_opy_:
            if fw in framework:
                bstack11ll1l11l1l_opy_ = True
        return bstack111ll11ll_opy_(bs_config.get(bstack1l1lll1_opy_ (u"࠭ࡴࡦࡵࡷࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ᫧"), bstack11ll1l11l1l_opy_))
    @classmethod
    def bstack11l11l1ll1l_opy_(cls, framework):
        return framework in bstack11l1l111ll1_opy_
    @classmethod
    def bstack11l11l11lll_opy_(cls, bs_config, framework):
        return cls.bstack11l11l1l11l_opy_(bs_config, framework) is True and cls.bstack11l11l1ll1l_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫ᫨"), None)
    @staticmethod
    def bstack1ll1lll1_opy_():
        if getattr(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬ᫩"), None):
            return {
                bstack1l1lll1_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ᫪"): bstack1l1lll1_opy_ (u"ࠪࡸࡪࡹࡴࠨ᫫"),
                bstack1l1lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ᫬"): getattr(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ᫭"), None)
            }
        if getattr(threading.current_thread(), bstack1l1lll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪ᫮"), None):
            return {
                bstack1l1lll1_opy_ (u"ࠧࡵࡻࡳࡩࠬ᫯"): bstack1l1lll1_opy_ (u"ࠨࡪࡲࡳࡰ࠭᫰"),
                bstack1l1lll1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ᫱"): getattr(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧ᫲"), None)
            }
        return None
    @staticmethod
    def bstack11l11l1ll11_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l11lll1_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1l1ll11l_opy_(test, hook_name=None):
        bstack11l11l1l1ll_opy_ = test.parent
        if hook_name in [bstack1l1lll1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠩ᫳"), bstack1l1lll1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡤ࡮ࡤࡷࡸ࠭᫴"), bstack1l1lll1_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࠬ᫵"), bstack1l1lll1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡳࡩࡻ࡬ࡦࠩ᫶")]:
            bstack11l11l1l1ll_opy_ = test
        scope = []
        while bstack11l11l1l1ll_opy_ is not None:
            scope.append(bstack11l11l1l1ll_opy_.name)
            bstack11l11l1l1ll_opy_ = bstack11l11l1l1ll_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11l11l1l1l1_opy_(hook_type):
        if hook_type == bstack1l1lll1_opy_ (u"ࠣࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍࠨ᫷"):
            return bstack1l1lll1_opy_ (u"ࠤࡖࡩࡹࡻࡰࠡࡪࡲࡳࡰࠨ᫸")
        elif hook_type == bstack1l1lll1_opy_ (u"ࠥࡅࡋ࡚ࡅࡓࡡࡈࡅࡈࡎࠢ᫹"):
            return bstack1l1lll1_opy_ (u"࡙ࠦ࡫ࡡࡳࡦࡲࡻࡳࠦࡨࡰࡱ࡮ࠦ᫺")
    @staticmethod
    def bstack11l11l11ll1_opy_(bstack1111l1ll_opy_):
        try:
            if not bstack1l11lll1_opy_.on():
                return bstack1111l1ll_opy_
            if os.environ.get(bstack1l1lll1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࠥ᫻"), None) == bstack1l1lll1_opy_ (u"ࠨࡴࡳࡷࡨࠦ᫼"):
                tests = os.environ.get(bstack1l1lll1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࡤ࡚ࡅࡔࡖࡖࠦ᫽"), None)
                if tests is None or tests == bstack1l1lll1_opy_ (u"ࠣࡰࡸࡰࡱࠨ᫾"):
                    return bstack1111l1ll_opy_
                bstack1111l1ll_opy_ = tests.split(bstack1l1lll1_opy_ (u"ࠩ࠯ࠫ᫿"))
                return bstack1111l1ll_opy_
        except Exception as exc:
            logger.debug(bstack1l1lll1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡵࡩࡷࡻ࡮ࠡࡪࡤࡲࡩࡲࡥࡳ࠼ࠣࠦᬀ") + str(str(exc)) + bstack1l1lll1_opy_ (u"ࠦࠧᬁ"))
        return bstack1111l1ll_opy_