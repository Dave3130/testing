# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
import os
import threading
from bstack_utils.helper import bstack1l11111l1l_opy_
from bstack_utils.constants import bstack11l1l1111l1_opy_, EVENTS, STAGE
from bstack_utils.bstack111ll1ll1l_opy_ import get_logger
logger = get_logger(__name__)
class bstack11llll11_opy_:
    bstack11l11l1l111_opy_ = None
    @classmethod
    def bstack11ll1l111_opy_(cls):
        if cls.on() and os.getenv(bstack11111_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉࠨ᫔")):
            logger.info(
                bstack11111_opy_ (u"࡙ࠩ࡭ࡸ࡯ࡴࠡࡪࡷࡸࡵࡹ࠺࠰࠱ࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁࠥࡺ࡯ࠡࡸ࡬ࡩࡼࠦࡢࡶ࡫࡯ࡨࠥࡸࡥࡱࡱࡵࡸ࠱ࠦࡩ࡯ࡵ࡬࡫࡭ࡺࡳ࠭ࠢࡤࡲࡩࠦ࡭ࡢࡰࡼࠤࡲࡵࡲࡦࠢࡧࡩࡧࡻࡧࡨ࡫ࡱ࡫ࠥ࡯࡮ࡧࡱࡵࡱࡦࡺࡩࡰࡰࠣࡥࡱࡲࠠࡢࡶࠣࡳࡳ࡫ࠠࡱ࡮ࡤࡧࡪࠧ࡜࡯ࠩ᫕").format(os.getenv(bstack11111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠣ᫖"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ᫗"), None) is None or os.environ[bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ᫘")] == bstack11111_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ᫙"):
            return False
        return True
    @classmethod
    def bstack11l11l11ll1_opy_(cls, bs_config, framework=bstack11111_opy_ (u"ࠢࠣ᫚")):
        bstack11ll1l111ll_opy_ = False
        for fw in bstack11l1l1111l1_opy_:
            if fw in framework:
                bstack11ll1l111ll_opy_ = True
        return bstack1l11111l1l_opy_(bs_config.get(bstack11111_opy_ (u"ࠨࡶࡨࡷࡹࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ᫛"), bstack11ll1l111ll_opy_))
    @classmethod
    def bstack11l11l1ll11_opy_(cls, framework):
        return framework in bstack11l1l1111l1_opy_
    @classmethod
    def bstack11l11l1l1l1_opy_(cls, bs_config, framework):
        return cls.bstack11l11l11ll1_opy_(bs_config, framework) is True and cls.bstack11l11l1ll11_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack11111_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭᫜"), None)
    @staticmethod
    def bstack11lll1l1_opy_():
        if getattr(threading.current_thread(), bstack11111_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧ᫝"), None):
            return {
                bstack11111_opy_ (u"ࠫࡹࡿࡰࡦࠩ᫞"): bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࠪ᫟"),
                bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭᫠"): getattr(threading.current_thread(), bstack11111_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫ᫡"), None)
            }
        if getattr(threading.current_thread(), bstack11111_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬ᫢"), None):
            return {
                bstack11111_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ᫣"): bstack11111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨ᫤"),
                bstack11111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ᫥"): getattr(threading.current_thread(), bstack11111_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ᫦"), None)
            }
        return None
    @staticmethod
    def bstack11l11l1l1ll_opy_(func):
        def wrap(*args, **kwargs):
            if bstack11llll11_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1ll1l111_opy_(test, hook_name=None):
        bstack11l11l1l11l_opy_ = test.parent
        if hook_name in [bstack11111_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡩ࡬ࡢࡵࡶࠫ᫧"), bstack11111_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠨ᫨"), bstack11111_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠧ᫩"), bstack11111_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫ᫪")]:
            bstack11l11l1l11l_opy_ = test
        scope = []
        while bstack11l11l1l11l_opy_ is not None:
            scope.append(bstack11l11l1l11l_opy_.name)
            bstack11l11l1l11l_opy_ = bstack11l11l1l11l_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11l11l11lll_opy_(hook_type):
        if hook_type == bstack11111_opy_ (u"ࠥࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠣ᫫"):
            return bstack11111_opy_ (u"ࠦࡘ࡫ࡴࡶࡲࠣ࡬ࡴࡵ࡫ࠣ᫬")
        elif hook_type == bstack11111_opy_ (u"ࠧࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠤ᫭"):
            return bstack11111_opy_ (u"ࠨࡔࡦࡣࡵࡨࡴࡽ࡮ࠡࡪࡲࡳࡰࠨ᫮")
    @staticmethod
    def bstack11l11l1ll1l_opy_(bstack1llll1lll_opy_):
        try:
            if not bstack11llll11_opy_.on():
                return bstack1llll1lll_opy_
            if os.environ.get(bstack11111_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࠧ᫯"), None) == bstack11111_opy_ (u"ࠣࡶࡵࡹࡪࠨ᫰"):
                tests = os.environ.get(bstack11111_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔ࡟ࡕࡇࡖࡘࡘࠨ᫱"), None)
                if tests is None or tests == bstack11111_opy_ (u"ࠥࡲࡺࡲ࡬ࠣ᫲"):
                    return bstack1llll1lll_opy_
                bstack1llll1lll_opy_ = tests.split(bstack11111_opy_ (u"ࠫ࠱࠭᫳"))
                return bstack1llll1lll_opy_
        except Exception as exc:
            logger.debug(bstack11111_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡷ࡫ࡲࡶࡰࠣ࡬ࡦࡴࡤ࡭ࡧࡵ࠾ࠥࠨ᫴") + str(str(exc)) + bstack11111_opy_ (u"ࠨࠢ᫵"))
        return bstack1llll1lll_opy_