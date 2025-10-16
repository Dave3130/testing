# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1ll1ll_opy_ import bstack1llllllll11_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1ll1l_opy_ import (
    bstack11111111ll_opy_,
    bstack1lllllll1ll_opy_,
    bstack1llllll11ll_opy_,
)
from bstack_utils.helper import  bstack1l1lll11_opy_
from browserstack_sdk.sdk_cli.bstack1lllllll11l_opy_ import bstack111111111l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l11lll_opy_, bstack1llll1l1111_opy_, bstack1llll1l11l1_opy_, bstack1ll11l1l11l_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack1l111ll1l_opy_ import bstack1111l1l1l_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l1111_opy_ import bstack1lll11llll1_opy_
from bstack_utils.percy import bstack1ll11l1111_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1l1l111l11l_opy_(bstack1llllllll11_opy_):
    def __init__(self, bstack11llllll1l1_opy_: Dict[str, str]):
        super().__init__()
        self.bstack11llllll1l1_opy_ = bstack11llllll1l1_opy_
        self.percy = bstack1ll11l1111_opy_()
        self.bstack1111l1ll11_opy_ = bstack1111l1l1l_opy_()
        self.bstack11llllll11l_opy_()
        bstack111111111l_opy_.bstack1llllll1l1l_opy_((bstack11111111ll_opy_.bstack1llll1l1ll1_opy_, bstack1lllllll1ll_opy_.PRE), self.bstack1l111111111_opy_)
        TestFramework.bstack1llllll1l1l_opy_((bstack1lll1l11lll_opy_.TEST, bstack1llll1l11l1_opy_.POST), self.bstack1llll11l1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l1l1l11_opy_(self, instance: bstack1llllll11ll_opy_, driver: object):
        bstack1l11ll111l1_opy_ = TestFramework.bstack1l11ll11111_opy_(instance.context)
        for t in bstack1l11ll111l1_opy_:
            bstack1lll11lll1l_opy_ = TestFramework.get_state(t, bstack1lll11llll1_opy_.bstack1llll11llll_opy_, [])
            if any(instance is d[1] for d in bstack1lll11lll1l_opy_) or instance == driver:
                return t
    def bstack1l111111111_opy_(
        self,
        f: bstack111111111l_opy_,
        driver: object,
        exec: Tuple[bstack1llllll11ll_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack11111111ll_opy_, bstack1lllllll1ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack111111111l_opy_.bstack1l1lll11111_opy_(method_name):
                return
            platform_index = f.get_state(instance, bstack111111111l_opy_.bstack1111111ll1_opy_, 0)
            bstack1ll1ll11l1l_opy_ = self.bstack1l11l1l1l11_opy_(instance, driver)
            bstack11lllllll1l_opy_ = TestFramework.get_state(bstack1ll1ll11l1l_opy_, TestFramework.bstack1ll11lll11l_opy_, None)
            if not bstack11lllllll1l_opy_:
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨ࡯࡯ࡡࡳࡶࡪࡥࡥࡹࡧࡦࡹࡹ࡫࠺ࠡࡴࡨࡸࡺࡸ࡮ࡪࡰࡪࠤࡦࡹࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡ࡫ࡶࠤࡳࡵࡴࠡࡻࡨࡸࠥࡹࡴࡢࡴࡷࡩࡩࠨᔛ"))
                return
            driver_command = f.bstack1l1lll11lll_opy_(*args)
            for command in bstack111l1l1l1_opy_:
                if command == driver_command:
                    self.bstack111ll1l1l1_opy_(driver, platform_index)
            bstack1lll1111l1_opy_ = self.percy.bstack1l1l111lll_opy_()
            if driver_command in bstack11l1ll111l_opy_[bstack1lll1111l1_opy_]:
                self.bstack1111l1ll11_opy_.bstack1l1l11lll_opy_(bstack11lllllll1l_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack1ll1ll1_opy_ (u"ࠢࡰࡰࡢࡴࡷ࡫࡟ࡦࡺࡨࡧࡺࡺࡥ࠻ࠢࡨࡶࡷࡵࡲࠣᔜ"), e)
    def bstack1llll11l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1111_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack111l11l1ll_opy_ import bstack1lllll1l11l_opy_
        bstack1lll11lll1l_opy_ = f.get_state(instance, bstack1lll11llll1_opy_.bstack1llll11llll_opy_, [])
        if not bstack1lll11lll1l_opy_:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᔝ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠤࠥᔞ"))
            return
        if len(bstack1lll11lll1l_opy_) > 1:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࢀࡲࡥ࡯ࠪࡧࡶ࡮ࡼࡥࡳࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᔟ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠦࠧᔠ"))
        bstack1lll111llll_opy_, bstack1lll1ll11l1_opy_ = bstack1lll11lll1l_opy_[0]
        driver = bstack1lll111llll_opy_()
        if not driver:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᔡ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠨࠢᔢ"))
            return
        bstack1l1111111l1_opy_ = {
            TestFramework.bstack1ll11l11l11_opy_: bstack1ll1ll1_opy_ (u"ࠢࡵࡧࡶࡸࠥࡴࡡ࡮ࡧࠥᔣ"),
            TestFramework.bstack1lll1l1l1l1_opy_: bstack1ll1ll1_opy_ (u"ࠣࡶࡨࡷࡹࠦࡵࡶ࡫ࡧࠦᔤ"),
            TestFramework.bstack1ll11lll11l_opy_: bstack1ll1ll1_opy_ (u"ࠤࡷࡩࡸࡺࠠࡳࡧࡵࡹࡳࠦ࡮ࡢ࡯ࡨࠦᔥ")
        }
        bstack11llllll1ll_opy_ = { key: f.get_state(instance, key) for key in bstack1l1111111l1_opy_ }
        bstack11llllllll1_opy_ = [key for key, value in bstack11llllll1ll_opy_.items() if not value]
        if bstack11llllllll1_opy_:
            for key in bstack11llllllll1_opy_:
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥࠨᔦ") + str(key) + bstack1ll1ll1_opy_ (u"ࠦࠧᔧ"))
            return
        platform_index = f.get_state(instance, bstack111111111l_opy_.bstack1111111ll1_opy_, 0)
        if self.bstack11llllll1l1_opy_.percy_capture_mode == bstack1ll1ll1_opy_ (u"ࠧࡺࡥࡴࡶࡦࡥࡸ࡫ࠢᔨ"):
            bstack1l111lll1l_opy_ = bstack11llllll1ll_opy_.get(TestFramework.bstack1ll11lll11l_opy_) + bstack1ll1ll1_opy_ (u"ࠨ࠭ࡵࡧࡶࡸࡨࡧࡳࡦࠤᔩ")
            bstack1ll111l11ll_opy_ = bstack1lllll1l11l_opy_.bstack1ll11l11l1l_opy_(EVENTS.bstack11lllllllll_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack1l111lll1l_opy_,
                bstack1l1l11111_opy_=bstack11llllll1ll_opy_[TestFramework.bstack1ll11l11l11_opy_],
                bstack1llllll111_opy_=bstack11llllll1ll_opy_[TestFramework.bstack1lll1l1l1l1_opy_],
                bstack111lll11l1_opy_=platform_index
            )
            bstack1lllll1l11l_opy_.end(EVENTS.bstack11lllllllll_opy_.value, bstack1ll111l11ll_opy_+bstack1ll1ll1_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᔪ"), bstack1ll111l11ll_opy_+bstack1ll1ll1_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᔫ"), True, None, None, None, None, test_name=bstack1l111lll1l_opy_)
    def bstack111ll1l1l1_opy_(self, driver, platform_index):
        if self.bstack1111l1ll11_opy_.bstack1ll111lll_opy_() is True or self.bstack1111l1ll11_opy_.capturing() is True:
            return
        self.bstack1111l1ll11_opy_.bstack1ll11llll_opy_()
        while not self.bstack1111l1ll11_opy_.bstack1ll111lll_opy_():
            bstack11lllllll1l_opy_ = self.bstack1111l1ll11_opy_.bstack111l1lllll_opy_()
            self.bstack1l11lllll1_opy_(driver, bstack11lllllll1l_opy_, platform_index)
        self.bstack1111l1ll11_opy_.bstack1lllll1l11_opy_()
    def bstack1l11lllll1_opy_(self, driver, bstack1111l1111_opy_, platform_index, test=None):
        from bstack_utils.bstack111l11l1ll_opy_ import bstack1lllll1l11l_opy_
        bstack1ll111l11ll_opy_ = bstack1lllll1l11l_opy_.bstack1ll11l11l1l_opy_(EVENTS.bstack1ll11l1ll1_opy_.value)
        if test != None:
            bstack1l1l11111_opy_ = getattr(test, bstack1ll1ll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᔬ"), None)
            bstack1llllll111_opy_ = getattr(test, bstack1ll1ll1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᔭ"), None)
            PercySDK.screenshot(driver, bstack1111l1111_opy_, bstack1l1l11111_opy_=bstack1l1l11111_opy_, bstack1llllll111_opy_=bstack1llllll111_opy_, bstack111lll11l1_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack1111l1111_opy_)
        bstack1lllll1l11l_opy_.end(EVENTS.bstack1ll11l1ll1_opy_.value, bstack1ll111l11ll_opy_+bstack1ll1ll1_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᔮ"), bstack1ll111l11ll_opy_+bstack1ll1ll1_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᔯ"), True, None, None, None, None, test_name=bstack1111l1111_opy_)
    def bstack11llllll11l_opy_(self):
        os.environ[bstack1ll1ll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࠫᔰ")] = str(self.bstack11llllll1l1_opy_.success)
        os.environ[bstack1ll1ll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࡤࡉࡁࡑࡖࡘࡖࡊࡥࡍࡐࡆࡈࠫᔱ")] = str(self.bstack11llllll1l1_opy_.percy_capture_mode)
        self.percy.bstack1l11111111l_opy_(self.bstack11llllll1l1_opy_.is_percy_auto_enabled)
        self.percy.bstack11lllllll11_opy_(self.bstack11llllll1l1_opy_.percy_build_id)