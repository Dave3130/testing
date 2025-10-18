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
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1l11l1_opy_ import bstack1111111ll1_opy_
from browserstack_sdk.sdk_cli.bstack111111l11l_opy_ import (
    bstack1llll1lll11_opy_,
    bstack1llll1ll111_opy_,
    bstack1llllllll1l_opy_,
)
from bstack_utils.helper import  bstack1l1l1l1l_opy_
from browserstack_sdk.sdk_cli.bstack1lllllllll1_opy_ import bstack1lllll111l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll11ll_opy_, bstack1lll1llll11_opy_, bstack1lll1lll11l_opy_, bstack1ll11ll1ll1_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack1111l1ll1_opy_ import bstack1l1llllll_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l11l1_opy_ import bstack1lll111l11l_opy_
from bstack_utils.percy import bstack11ll111l1l_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1l1l11111ll_opy_(bstack1111111ll1_opy_):
    def __init__(self, bstack11lllll1lll_opy_: Dict[str, str]):
        super().__init__()
        self.bstack11lllll1lll_opy_ = bstack11lllll1lll_opy_
        self.percy = bstack11ll111l1l_opy_()
        self.bstack1l11l11l1l_opy_ = bstack1l1llllll_opy_()
        self.bstack11llllllll1_opy_()
        bstack1lllll111l1_opy_.bstack1llllll1111_opy_((bstack1llll1lll11_opy_.bstack1llllllllll_opy_, bstack1llll1ll111_opy_.PRE), self.bstack11llllll1l1_opy_)
        TestFramework.bstack1llllll1111_opy_((bstack1lll1ll11ll_opy_.TEST, bstack1lll1lll11l_opy_.POST), self.bstack1llll111l1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l11ll11111_opy_(self, instance: bstack1llllllll1l_opy_, driver: object):
        bstack1l11l1l1l11_opy_ = TestFramework.bstack1l11l1l1111_opy_(instance.context)
        for t in bstack1l11l1l1l11_opy_:
            bstack1lll11l111l_opy_ = TestFramework.get_state(t, bstack1lll111l11l_opy_.bstack1lll1llllll_opy_, [])
            if any(instance is d[1] for d in bstack1lll11l111l_opy_) or instance == driver:
                return t
    def bstack11llllll1l1_opy_(
        self,
        f: bstack1lllll111l1_opy_,
        driver: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1lllll1llll_opy_: Tuple[bstack1llll1lll11_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1lllll111l1_opy_.bstack1l1lll1lll1_opy_(method_name):
                return
            platform_index = f.get_state(instance, bstack1lllll111l1_opy_.bstack1llll1l1ll1_opy_, 0)
            bstack1ll1l1111ll_opy_ = self.bstack1l11ll11111_opy_(instance, driver)
            bstack11llllll111_opy_ = TestFramework.get_state(bstack1ll1l1111ll_opy_, TestFramework.bstack1ll111ll1l1_opy_, None)
            if not bstack11llllll111_opy_:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡰࡰࡢࡴࡷ࡫࡟ࡦࡺࡨࡧࡺࡺࡥ࠻ࠢࡵࡩࡹࡻࡲ࡯࡫ࡱ࡫ࠥࡧࡳࠡࡵࡨࡷࡸ࡯࡯࡯ࠢ࡬ࡷࠥࡴ࡯ࡵࠢࡼࡩࡹࠦࡳࡵࡣࡵࡸࡪࡪࠢᔕ"))
                return
            driver_command = f.bstack1l1llll11l1_opy_(*args)
            for command in bstack111l11l111_opy_:
                if command == driver_command:
                    self.bstack1ll1ll111_opy_(driver, platform_index)
            bstack111lll1l1l_opy_ = self.percy.bstack11l1ll11l1_opy_()
            if driver_command in bstack11lllll11_opy_[bstack111lll1l1l_opy_]:
                self.bstack1l11l11l1l_opy_.bstack1ll111l1l1_opy_(bstack11llllll111_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠣࡱࡱࡣࡵࡸࡥࡠࡧࡻࡩࡨࡻࡴࡦ࠼ࠣࡩࡷࡸ࡯ࡳࠤᔖ"), e)
    def bstack1llll111l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1llll11_opy_,
        bstack1lllll1llll_opy_: Tuple[bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack11l1l1111l_opy_ import bstack1llll1ll11l_opy_
        bstack1lll11l111l_opy_ = f.get_state(instance, bstack1lll111l11l_opy_.bstack1lll1llllll_opy_, [])
        if not bstack1lll11l111l_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᔗ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠥࠦᔘ"))
            return
        if len(bstack1lll11l111l_opy_) > 1:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࢁ࡬ࡦࡰࠫࡨࡷ࡯ࡶࡦࡴࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᔙ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠧࠨᔚ"))
        bstack1lll11ll111_opy_, bstack1lll1ll1lll_opy_ = bstack1lll11l111l_opy_[0]
        driver = bstack1lll11ll111_opy_()
        if not driver:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᔛ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠢࠣᔜ"))
            return
        bstack11llllll11l_opy_ = {
            TestFramework.bstack1ll11ll11l1_opy_: bstack1l1lll1_opy_ (u"ࠣࡶࡨࡷࡹࠦ࡮ࡢ࡯ࡨࠦᔝ"),
            TestFramework.bstack1llll11lll1_opy_: bstack1l1lll1_opy_ (u"ࠤࡷࡩࡸࡺࠠࡶࡷ࡬ࡨࠧᔞ"),
            TestFramework.bstack1ll111ll1l1_opy_: bstack1l1lll1_opy_ (u"ࠥࡸࡪࡹࡴࠡࡴࡨࡶࡺࡴࠠ࡯ࡣࡰࡩࠧᔟ")
        }
        bstack11lllllll1l_opy_ = { key: f.get_state(instance, key) for key in bstack11llllll11l_opy_ }
        bstack11lllllll11_opy_ = [key for key, value in bstack11lllllll1l_opy_.items() if not value]
        if bstack11lllllll11_opy_:
            for key in bstack11lllllll11_opy_:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࠢᔠ") + str(key) + bstack1l1lll1_opy_ (u"ࠧࠨᔡ"))
            return
        platform_index = f.get_state(instance, bstack1lllll111l1_opy_.bstack1llll1l1ll1_opy_, 0)
        if self.bstack11lllll1lll_opy_.percy_capture_mode == bstack1l1lll1_opy_ (u"ࠨࡴࡦࡵࡷࡧࡦࡹࡥࠣᔢ"):
            bstack11ll1l1ll1_opy_ = bstack11lllllll1l_opy_.get(TestFramework.bstack1ll111ll1l1_opy_) + bstack1l1lll1_opy_ (u"ࠢ࠮ࡶࡨࡷࡹࡩࡡࡴࡧࠥᔣ")
            bstack1ll1l11l111_opy_ = bstack1llll1ll11l_opy_.bstack1ll1ll1111l_opy_(EVENTS.bstack11llllll1ll_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack11ll1l1ll1_opy_,
                bstack1111l11ll_opy_=bstack11lllllll1l_opy_[TestFramework.bstack1ll11ll11l1_opy_],
                bstack1l1lll111l_opy_=bstack11lllllll1l_opy_[TestFramework.bstack1llll11lll1_opy_],
                bstack1l111l111l_opy_=platform_index
            )
            bstack1llll1ll11l_opy_.end(EVENTS.bstack11llllll1ll_opy_.value, bstack1ll1l11l111_opy_+bstack1l1lll1_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᔤ"), bstack1ll1l11l111_opy_+bstack1l1lll1_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᔥ"), True, None, None, None, None, test_name=bstack11ll1l1ll1_opy_)
    def bstack1ll1ll111_opy_(self, driver, platform_index):
        if self.bstack1l11l11l1l_opy_.bstack1111l1lll_opy_() is True or self.bstack1l11l11l1l_opy_.capturing() is True:
            return
        self.bstack1l11l11l1l_opy_.bstack1lllll1l1l_opy_()
        while not self.bstack1l11l11l1l_opy_.bstack1111l1lll_opy_():
            bstack11llllll111_opy_ = self.bstack1l11l11l1l_opy_.bstack1111l1l111_opy_()
            self.bstack1l11l11l1_opy_(driver, bstack11llllll111_opy_, platform_index)
        self.bstack1l11l11l1l_opy_.bstack1ll1l111ll_opy_()
    def bstack1l11l11l1_opy_(self, driver, bstack11111llll1_opy_, platform_index, test=None):
        from bstack_utils.bstack11l1l1111l_opy_ import bstack1llll1ll11l_opy_
        bstack1ll1l11l111_opy_ = bstack1llll1ll11l_opy_.bstack1ll1ll1111l_opy_(EVENTS.bstack1l1ll11l1l_opy_.value)
        if test != None:
            bstack1111l11ll_opy_ = getattr(test, bstack1l1lll1_opy_ (u"ࠪࡲࡦࡳࡥࠨᔦ"), None)
            bstack1l1lll111l_opy_ = getattr(test, bstack1l1lll1_opy_ (u"ࠫࡺࡻࡩࡥࠩᔧ"), None)
            PercySDK.screenshot(driver, bstack11111llll1_opy_, bstack1111l11ll_opy_=bstack1111l11ll_opy_, bstack1l1lll111l_opy_=bstack1l1lll111l_opy_, bstack1l111l111l_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack11111llll1_opy_)
        bstack1llll1ll11l_opy_.end(EVENTS.bstack1l1ll11l1l_opy_.value, bstack1ll1l11l111_opy_+bstack1l1lll1_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᔨ"), bstack1ll1l11l111_opy_+bstack1l1lll1_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᔩ"), True, None, None, None, None, test_name=bstack11111llll1_opy_)
    def bstack11llllllll1_opy_(self):
        os.environ[bstack1l1lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࠬᔪ")] = str(self.bstack11lllll1lll_opy_.success)
        os.environ[bstack1l1lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡇࡕࡇ࡞ࡥࡃࡂࡒࡗ࡙ࡗࡋ࡟ࡎࡑࡇࡉࠬᔫ")] = str(self.bstack11lllll1lll_opy_.percy_capture_mode)
        self.percy.bstack11lllll1ll1_opy_(self.bstack11lllll1lll_opy_.is_percy_auto_enabled)
        self.percy.bstack11lllllllll_opy_(self.bstack11lllll1lll_opy_.percy_build_id)