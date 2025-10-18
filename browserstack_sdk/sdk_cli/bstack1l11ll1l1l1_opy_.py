# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lllllll11l_opy_ import bstack1lllllllll1_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1l1l_opy_ import (
    bstack1llll1ll1l1_opy_,
    bstack1lllll1ll1l_opy_,
    bstack1lllll11l1l_opy_,
)
from bstack_utils.helper import  bstack1l1l11l1_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1ll1_opy_ import bstack1lllll1l1l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1ll11_opy_, bstack1llll1111l1_opy_, bstack1lll1ll111l_opy_, bstack1ll11l111l1_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack111llll111_opy_ import bstack1ll1ll1l11_opy_
from browserstack_sdk.sdk_cli.bstack1lll111l1l1_opy_ import bstack1lll11l1111_opy_
from bstack_utils.percy import bstack111l1l1ll1_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1l1l1l111ll_opy_(bstack1lllllllll1_opy_):
    def __init__(self, bstack11lllll111l_opy_: Dict[str, str]):
        super().__init__()
        self.bstack11lllll111l_opy_ = bstack11lllll111l_opy_
        self.percy = bstack111l1l1ll1_opy_()
        self.bstack111l1ll11l_opy_ = bstack1ll1ll1l11_opy_()
        self.bstack11lllll1ll1_opy_()
        bstack1lllll1l1l1_opy_.bstack1lllll1l1ll_opy_((bstack1llll1ll1l1_opy_.bstack1llll1lllll_opy_, bstack1lllll1ll1l_opy_.PRE), self.bstack11lllll11l1_opy_)
        TestFramework.bstack1lllll1l1ll_opy_((bstack1lll1l1ll11_opy_.TEST, bstack1lll1ll111l_opy_.POST), self.bstack1lll1l11lll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l111llll1l_opy_(self, instance: bstack1lllll11l1l_opy_, driver: object):
        bstack1l111lll111_opy_ = TestFramework.bstack1l111ll1lll_opy_(instance.context)
        for t in bstack1l111lll111_opy_:
            bstack1lll1111l1l_opy_ = TestFramework.get_state(t, bstack1lll11l1111_opy_.bstack1lll1l1llll_opy_, [])
            if any(instance is d[1] for d in bstack1lll1111l1l_opy_) or instance == driver:
                return t
    def bstack11lllll11l1_opy_(
        self,
        f: bstack1lllll1l1l1_opy_,
        driver: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l11l_opy_: Tuple[bstack1llll1ll1l1_opy_, bstack1lllll1ll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1lllll1l1l1_opy_.bstack1l1ll1ll11l_opy_(method_name):
                return
            platform_index = f.get_state(instance, bstack1lllll1l1l1_opy_.bstack1llll1l111l_opy_, 0)
            bstack1ll11l1llll_opy_ = self.bstack1l111llll1l_opy_(instance, driver)
            bstack11llll1ll1l_opy_ = TestFramework.get_state(bstack1ll11l1llll_opy_, TestFramework.bstack1ll111ll11l_opy_, None)
            if not bstack11llll1ll1l_opy_:
                self.logger.debug(bstack11ll_opy_ (u"ࠨ࡯࡯ࡡࡳࡶࡪࡥࡥࡹࡧࡦࡹࡹ࡫࠺ࠡࡴࡨࡸࡺࡸ࡮ࡪࡰࡪࠤࡦࡹࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡ࡫ࡶࠤࡳࡵࡴࠡࡻࡨࡸࠥࡹࡴࡢࡴࡷࡩࡩࠨᔾ"))
                return
            driver_command = f.bstack1l1lll11l11_opy_(*args)
            for command in bstack1111ll1lll_opy_:
                if command == driver_command:
                    self.bstack11l111l1l1_opy_(driver, platform_index)
            bstack11ll1ll1l_opy_ = self.percy.bstack11111lllll_opy_()
            if driver_command in bstack1l11111l11_opy_[bstack11ll1ll1l_opy_]:
                self.bstack111l1ll11l_opy_.bstack11l1ll1l1_opy_(bstack11llll1ll1l_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack11ll_opy_ (u"ࠢࡰࡰࡢࡴࡷ࡫࡟ࡦࡺࡨࡧࡺࡺࡥ࠻ࠢࡨࡶࡷࡵࡲࠣᔿ"), e)
    def bstack1lll1l11lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111l1_opy_,
        bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack11l1l1ll11_opy_ import bstack1llll11ll11_opy_
        bstack1lll1111l1l_opy_ = f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll1l1llll_opy_, [])
        if not bstack1lll1111l1l_opy_:
            self.logger.debug(bstack11ll_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᕀ") + str(kwargs) + bstack11ll_opy_ (u"ࠤࠥᕁ"))
            return
        if len(bstack1lll1111l1l_opy_) > 1:
            self.logger.debug(bstack11ll_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࢀࡲࡥ࡯ࠪࡧࡶ࡮ࡼࡥࡳࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᕂ") + str(kwargs) + bstack11ll_opy_ (u"ࠦࠧᕃ"))
        bstack1lll11l11l1_opy_, bstack1lll1l1lll1_opy_ = bstack1lll1111l1l_opy_[0]
        driver = bstack1lll11l11l1_opy_()
        if not driver:
            self.logger.debug(bstack11ll_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᕄ") + str(kwargs) + bstack11ll_opy_ (u"ࠨࠢᕅ"))
            return
        bstack11lllll11ll_opy_ = {
            TestFramework.bstack1ll11ll1ll1_opy_: bstack11ll_opy_ (u"ࠢࡵࡧࡶࡸࠥࡴࡡ࡮ࡧࠥᕆ"),
            TestFramework.bstack1llll111l11_opy_: bstack11ll_opy_ (u"ࠣࡶࡨࡷࡹࠦࡵࡶ࡫ࡧࠦᕇ"),
            TestFramework.bstack1ll111ll11l_opy_: bstack11ll_opy_ (u"ࠤࡷࡩࡸࡺࠠࡳࡧࡵࡹࡳࠦ࡮ࡢ࡯ࡨࠦᕈ")
        }
        bstack11llll1llll_opy_ = { key: f.get_state(instance, key) for key in bstack11lllll11ll_opy_ }
        bstack11lllll1111_opy_ = [key for key, value in bstack11llll1llll_opy_.items() if not value]
        if bstack11lllll1111_opy_:
            for key in bstack11lllll1111_opy_:
                self.logger.debug(bstack11ll_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥࠨᕉ") + str(key) + bstack11ll_opy_ (u"ࠦࠧᕊ"))
            return
        platform_index = f.get_state(instance, bstack1lllll1l1l1_opy_.bstack1llll1l111l_opy_, 0)
        if self.bstack11lllll111l_opy_.percy_capture_mode == bstack11ll_opy_ (u"ࠧࡺࡥࡴࡶࡦࡥࡸ࡫ࠢᕋ"):
            bstack111ll11l1_opy_ = bstack11llll1llll_opy_.get(TestFramework.bstack1ll111ll11l_opy_) + bstack11ll_opy_ (u"ࠨ࠭ࡵࡧࡶࡸࡨࡧࡳࡦࠤᕌ")
            bstack1ll111l11ll_opy_ = bstack1llll11ll11_opy_.bstack1ll11l1ll1l_opy_(EVENTS.bstack11llll1lll1_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack111ll11l1_opy_,
                bstack1ll11l111l_opy_=bstack11llll1llll_opy_[TestFramework.bstack1ll11ll1ll1_opy_],
                bstack111l1111l1_opy_=bstack11llll1llll_opy_[TestFramework.bstack1llll111l11_opy_],
                bstack1ll111lll1_opy_=platform_index
            )
            bstack1llll11ll11_opy_.end(EVENTS.bstack11llll1lll1_opy_.value, bstack1ll111l11ll_opy_+bstack11ll_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᕍ"), bstack1ll111l11ll_opy_+bstack11ll_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᕎ"), True, None, None, None, None, test_name=bstack111ll11l1_opy_)
    def bstack11l111l1l1_opy_(self, driver, platform_index):
        if self.bstack111l1ll11l_opy_.bstack11ll11111_opy_() is True or self.bstack111l1ll11l_opy_.capturing() is True:
            return
        self.bstack111l1ll11l_opy_.bstack1llll1ll1l_opy_()
        while not self.bstack111l1ll11l_opy_.bstack11ll11111_opy_():
            bstack11llll1ll1l_opy_ = self.bstack111l1ll11l_opy_.bstack111ll11l1l_opy_()
            self.bstack1ll1ll1ll_opy_(driver, bstack11llll1ll1l_opy_, platform_index)
        self.bstack111l1ll11l_opy_.bstack1l1ll1lll_opy_()
    def bstack1ll1ll1ll_opy_(self, driver, bstack1l1l1l1l11_opy_, platform_index, test=None):
        from bstack_utils.bstack11l1l1ll11_opy_ import bstack1llll11ll11_opy_
        bstack1ll111l11ll_opy_ = bstack1llll11ll11_opy_.bstack1ll11l1ll1l_opy_(EVENTS.bstack111ll11lll_opy_.value)
        if test != None:
            bstack1ll11l111l_opy_ = getattr(test, bstack11ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᕏ"), None)
            bstack111l1111l1_opy_ = getattr(test, bstack11ll_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᕐ"), None)
            PercySDK.screenshot(driver, bstack1l1l1l1l11_opy_, bstack1ll11l111l_opy_=bstack1ll11l111l_opy_, bstack111l1111l1_opy_=bstack111l1111l1_opy_, bstack1ll111lll1_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack1l1l1l1l11_opy_)
        bstack1llll11ll11_opy_.end(EVENTS.bstack111ll11lll_opy_.value, bstack1ll111l11ll_opy_+bstack11ll_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᕑ"), bstack1ll111l11ll_opy_+bstack11ll_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᕒ"), True, None, None, None, None, test_name=bstack1l1l1l1l11_opy_)
    def bstack11lllll1ll1_opy_(self):
        os.environ[bstack11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࠫᕓ")] = str(self.bstack11lllll111l_opy_.success)
        os.environ[bstack11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࡤࡉࡁࡑࡖࡘࡖࡊࡥࡍࡐࡆࡈࠫᕔ")] = str(self.bstack11lllll111l_opy_.percy_capture_mode)
        self.percy.bstack11lllll1l11_opy_(self.bstack11lllll111l_opy_.is_percy_auto_enabled)
        self.percy.bstack11lllll1l1l_opy_(self.bstack11lllll111l_opy_.percy_build_id)