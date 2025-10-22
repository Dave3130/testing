# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1ll1lll1ll1_opy_ import bstack1ll1ll11ll1_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll11111l1_opy_ import bstack1l1lll1llll_opy_
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1llll111l1l_opy_,
    bstack1lll1l1llll_opy_,
    bstack1lll1lll111_opy_,
    bstack1ll11l11l11_opy_,
    bstack1ll1l1l1ll1_opy_,
)
import traceback
from bstack_utils.helper import bstack1ll1l1ll11l_opy_
from bstack_utils.bstack111l1111l_opy_ import bstack1llllllll1l_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.utils.bstack1l1lll1lll1_opy_ import bstack1ll1111ll11_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l1l11_opy_ import bstack1lll11l1l1l_opy_
bstack1ll11ll1111_opy_ = bstack1ll1l1ll11l_opy_()
bstack1ll11lll11l_opy_ = bstack1lllll1l_opy_ (u"ࠨࡕࡱ࡮ࡲࡥࡩ࡫ࡤࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷ࠲ࠨሙ")
bstack1ll11lll1l1_opy_ = bstack1lllll1l_opy_ (u"ࠢࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮ࠥሚ")
bstack1l1llll1111_opy_ = bstack1lllll1l_opy_ (u"ࠣࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࡍࡵ࡯࡬ࡇࡹࡩࡳࡺࠢማ")
bstack1ll1l11llll_opy_ = 1.0
_1ll111l11l1_opy_ = set()
class PytestBDDFramework(TestFramework):
    bstack1ll1l111ll1_opy_ = bstack1lllll1l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴࠤሜ")
    bstack1ll11l11ll1_opy_ = bstack1lllll1l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡹ࡟ࡴࡶࡤࡶࡹ࡫ࡤࠣም")
    bstack1l1llll1ll1_opy_ = bstack1lllll1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱࡳࡠࡨ࡬ࡲ࡮ࡹࡨࡦࡦࠥሞ")
    bstack1l1llll111l_opy_ = bstack1lllll1l_opy_ (u"ࠧࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠ࡮ࡤࡷࡹࡥࡳࡵࡣࡵࡸࡪࡪࠢሟ")
    bstack1ll111l1l11_opy_ = bstack1lllll1l_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡ࡯ࡥࡸࡺ࡟ࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࠤሠ")
    bstack1ll111111l1_opy_: bool
    bstack1lll11l1l11_opy_: bstack1lll11l1l1l_opy_  = None
    bstack1ll11l11l1l_opy_ = [
        bstack1llll111l1l_opy_.BEFORE_ALL,
        bstack1llll111l1l_opy_.AFTER_ALL,
        bstack1llll111l1l_opy_.BEFORE_EACH,
        bstack1llll111l1l_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll111llll1_opy_: Dict[str, str],
        bstack1ll1l1l11ll_opy_: List[str]=[bstack1lllll1l_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠦሡ")],
        bstack1lll11l1l11_opy_: bstack1lll11l1l1l_opy_ = None,
        bstack1lllllll111_opy_=None
    ):
        super().__init__(bstack1ll1l1l11ll_opy_, bstack1ll111llll1_opy_, bstack1lll11l1l11_opy_)
        self.bstack1ll111111l1_opy_ = any(bstack1lllll1l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠧሢ") in item.lower() for item in bstack1ll1l1l11ll_opy_)
        self.bstack1lllllll111_opy_ = bstack1lllllll111_opy_
    def track_event(
        self,
        context: bstack1ll11l11l11_opy_,
        test_framework_state: bstack1llll111l1l_opy_,
        test_hook_state: bstack1lll1lll111_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1llll111l1l_opy_.TEST or test_framework_state in PytestBDDFramework.bstack1ll11l11l1l_opy_:
            bstack1l1lll1llll_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1llll111l1l_opy_.NONE:
            self.logger.warning(bstack1lllll1l_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡦࡦࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯ࠥࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦ࠿ࠥሣ") + str(test_hook_state) + bstack1lllll1l_opy_ (u"ࠥࠦሤ"))
            return
        if not self.bstack1ll111111l1_opy_:
            self.logger.warning(bstack1lllll1l_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳࡹࡵࡱࡲࡲࡶࡹ࡫ࡤࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡁࠧሥ") + str(str(self.bstack1ll1l1l11ll_opy_)) + bstack1lllll1l_opy_ (u"ࠧࠨሦ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack1lllll1l_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡦࡺࡳࡩࡨࡺࡥࡥࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣሧ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠢࠣረ"))
            return
        instance = self.__1ll111l11ll_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰ࡫ࡥࡳࡪ࡬ࡦࡦࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡣࡵ࡫ࡸࡃࠢሩ") + str(args) + bstack1lllll1l_opy_ (u"ࠤࠥሪ"))
            return
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll11l11l1l_opy_ and test_hook_state == bstack1lll1lll111_opy_.PRE:
                bstack1ll111ll1l1_opy_ = bstack1llllllll1l_opy_.bstack1ll11l111l1_opy_(EVENTS.bstack11l1ll1lll_opy_.value)
                name = str(EVENTS.bstack11l1ll1lll_opy_.name)+bstack1lllll1l_opy_ (u"ࠥ࠾ࠧራ")+str(test_framework_state.name)
                TestFramework.bstack1ll1l1l1lll_opy_(instance, name, bstack1ll111ll1l1_opy_)
        except Exception as e:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣ࡬ࡴࡵ࡫ࠡࡧࡵࡶࡴࡸࠠࡱࡴࡨ࠾ࠥࢁࡽࠣሬ").format(e))
        try:
            if test_framework_state == bstack1llll111l1l_opy_.TEST:
                if not TestFramework.bstack1lllllll11l_opy_(instance, TestFramework.bstack1ll1l11lll1_opy_) and test_hook_state == bstack1lll1lll111_opy_.PRE:
                    if not (len(args) >= 3):
                        return
                    test = PytestBDDFramework.__1ll11lllll1_opy_(args)
                    if test:
                        instance.data.update(test)
                        self.logger.debug(bstack1lllll1l_opy_ (u"ࠧࡲ࡯ࡢࡦࡨࡨࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡶࡪ࡬ࠨࠪࡿࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࠧር") + str(test_hook_state) + bstack1lllll1l_opy_ (u"ࠨࠢሮ"))
                if test_hook_state == bstack1lll1lll111_opy_.PRE and not TestFramework.bstack1lllllll11l_opy_(instance, TestFramework.bstack1ll11l1lll1_opy_):
                    TestFramework.bstack1llll11ll1l_opy_(instance, TestFramework.bstack1ll11l1lll1_opy_, datetime.now(tz=timezone.utc))
                    PytestBDDFramework.__1ll111111ll_opy_(instance, args)
                    self.logger.debug(bstack1lllll1l_opy_ (u"ࠢࡴࡧࡷࠤࡹ࡫ࡳࡵ࠯ࡶࡸࡦࡸࡴࠡࡨࡲࡶࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡶࡪ࡬ࠨࠪࡿࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࠧሯ") + str(test_hook_state) + bstack1lllll1l_opy_ (u"ࠣࠤሰ"))
                elif test_hook_state == bstack1lll1lll111_opy_.POST and not TestFramework.bstack1lllllll11l_opy_(instance, TestFramework.bstack1ll1l11l1ll_opy_):
                    TestFramework.bstack1llll11ll1l_opy_(instance, TestFramework.bstack1ll1l11l1ll_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1lllll1l_opy_ (u"ࠤࡶࡩࡹࠦࡴࡦࡵࡷ࠱ࡪࡴࡤࠡࡨࡲࡶࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡶࡪ࡬ࠨࠪࡿࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࠧሱ") + str(test_hook_state) + bstack1lllll1l_opy_ (u"ࠥࠦሲ"))
            elif test_framework_state == bstack1llll111l1l_opy_.STEP:
                if test_hook_state == bstack1lll1lll111_opy_.PRE:
                    PytestBDDFramework.__1ll11ll1lll_opy_(instance, args)
                elif test_hook_state == bstack1lll1lll111_opy_.POST:
                    PytestBDDFramework.__1ll11l1ll11_opy_(instance, args)
            elif test_framework_state == bstack1llll111l1l_opy_.LOG and test_hook_state == bstack1lll1lll111_opy_.POST:
                PytestBDDFramework.__1ll111l1ll1_opy_(instance, *args)
            elif test_framework_state == bstack1llll111l1l_opy_.LOG_REPORT and test_hook_state == bstack1lll1lll111_opy_.POST:
                self.__1ll1l1l1l1l_opy_(instance, *args)
                self.__1ll1l1l1111_opy_(instance)
            elif test_framework_state in PytestBDDFramework.bstack1ll11l11l1l_opy_:
                self.__1ll11l1llll_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣ࡬ࡦࡴࡤ࡭ࡧࡧࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࠧሳ") + str(instance.ref()) + bstack1lllll1l_opy_ (u"ࠧࠨሴ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll11111111_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll11l11l1l_opy_ and test_hook_state == bstack1lll1lll111_opy_.POST:
                name = str(EVENTS.bstack11l1ll1lll_opy_.name)+bstack1lllll1l_opy_ (u"ࠨ࠺ࠣስ")+str(test_framework_state.name)
                bstack1ll111ll1l1_opy_ = TestFramework.bstack1ll1l111lll_opy_(instance, name)
                bstack1llllllll1l_opy_.end(EVENTS.bstack11l1ll1lll_opy_.value, bstack1ll111ll1l1_opy_+bstack1lllll1l_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢሶ"), bstack1ll111ll1l1_opy_+bstack1lllll1l_opy_ (u"ࠣ࠼ࡨࡲࡩࠨሷ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡪࡲࡳࡰࠦࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠤሸ").format(e))
    def bstack1l1lllll1ll_opy_(self):
        return self.bstack1ll111111l1_opy_
    def __1ll111ll111_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack1lllll1l_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡳࡧࡶࡹࡱࡺࠢሹ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll11l111ll_opy_(rep, [bstack1lllll1l_opy_ (u"ࠦࡼ࡮ࡥ࡯ࠤሺ"), bstack1lllll1l_opy_ (u"ࠧࡵࡵࡵࡥࡲࡱࡪࠨሻ"), bstack1lllll1l_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨሼ"), bstack1lllll1l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢሽ"), bstack1lllll1l_opy_ (u"ࠣࡵ࡮࡭ࡵࡶࡥࡥࠤሾ"), bstack1lllll1l_opy_ (u"ࠤ࡯ࡳࡳ࡭ࡲࡦࡲࡵࡸࡪࡾࡴࠣሿ")])
        return None
    def __1ll1l1l1l1l_opy_(self, instance: bstack1lll1l1llll_opy_, *args):
        result = self.__1ll111ll111_opy_(*args)
        if not result:
            return
        failure = None
        bstack111111l111_opy_ = None
        if result.get(bstack1lllll1l_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦቀ"), None) == bstack1lllll1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦቁ") and len(args) > 1 and getattr(args[1], bstack1lllll1l_opy_ (u"ࠧ࡫ࡸࡤ࡫ࡱࡪࡴࠨቂ"), None) is not None:
            failure = [{bstack1lllll1l_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩቃ"): [args[1].excinfo.exconly(), result.get(bstack1lllll1l_opy_ (u"ࠢ࡭ࡱࡱ࡫ࡷ࡫ࡰࡳࡶࡨࡼࡹࠨቄ"), None)]}]
            bstack111111l111_opy_ = bstack1lllll1l_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤቅ") if bstack1lllll1l_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧቆ") in getattr(args[1].excinfo, bstack1lllll1l_opy_ (u"ࠥࡸࡾࡶࡥ࡯ࡣࡰࡩࠧቇ"), bstack1lllll1l_opy_ (u"ࠦࠧቈ")) else bstack1lllll1l_opy_ (u"࡛ࠧ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࠨ቉")
        bstack1ll11ll11l1_opy_ = result.get(bstack1lllll1l_opy_ (u"ࠨ࡯ࡶࡶࡦࡳࡲ࡫ࠢቊ"), TestFramework.bstack1l1llllll11_opy_)
        if bstack1ll11ll11l1_opy_ != TestFramework.bstack1l1llllll11_opy_:
            TestFramework.bstack1llll11ll1l_opy_(instance, TestFramework.bstack1ll11llll11_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll1111l11l_opy_(instance, {
            TestFramework.bstack1lll11ll111_opy_: failure,
            TestFramework.bstack1l1llll11ll_opy_: bstack111111l111_opy_,
            TestFramework.bstack1lll1l1111l_opy_: bstack1ll11ll11l1_opy_,
        })
    def __1ll111l11ll_opy_(
        self,
        context: bstack1ll11l11l11_opy_,
        test_framework_state: bstack1llll111l1l_opy_,
        test_hook_state: bstack1lll1lll111_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1llll111l1l_opy_.SETUP_FIXTURE:
            instance = self.__1ll1l11111l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll11llll1l_opy_ bstack1ll1111l1l1_opy_ this to be bstack1lllll1l_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢቋ")
            if test_framework_state == bstack1llll111l1l_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1l1llll1lll_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1llll111l1l_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack1lllll1l_opy_ (u"ࠣࡰࡲࡨࡪࠨቌ"), None), bstack1lllll1l_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤቍ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack1lllll1l_opy_ (u"ࠥࡲࡴࡪࡥࠣ቎"), None):
                target = args[0].node.nodeid
            elif getattr(args[0], bstack1lllll1l_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦ቏"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1l1llllllll_opy_(target) if target else None
        return instance
    def __1ll11l1llll_opy_(
        self,
        instance: bstack1lll1l1llll_opy_,
        test_framework_state: bstack1llll111l1l_opy_,
        test_hook_state: bstack1lll1lll111_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll1l111111_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll11l11ll1_opy_, {})
        if not key in bstack1ll1l111111_opy_:
            bstack1ll1l111111_opy_[key] = []
        bstack1ll1l1l111l_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1l1llll1ll1_opy_, {})
        if not key in bstack1ll1l1l111l_opy_:
            bstack1ll1l1l111l_opy_[key] = []
        bstack1ll111ll11l_opy_ = {
            PytestBDDFramework.bstack1ll11l11ll1_opy_: bstack1ll1l111111_opy_,
            PytestBDDFramework.bstack1l1llll1ll1_opy_: bstack1ll1l1l111l_opy_,
        }
        if test_hook_state == bstack1lll1lll111_opy_.PRE:
            hook_name = args[1] if len(args) > 1 else None
            hook = {
                bstack1lllll1l_opy_ (u"ࠧࡱࡥࡺࠤቐ"): key,
                TestFramework.bstack1ll11l1ll1l_opy_: uuid4().__str__(),
                TestFramework.bstack1l1llll1l11_opy_: TestFramework.bstack1l1llll1l1l_opy_,
                TestFramework.bstack1ll1l11l1l1_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll111ll1ll_opy_: [],
                TestFramework.bstack1ll11lll111_opy_: hook_name,
                TestFramework.bstack1ll11111l1l_opy_: bstack1ll1111ll11_opy_.bstack1ll11llllll_opy_()
            }
            bstack1ll1l111111_opy_[key].append(hook)
            bstack1ll111ll11l_opy_[PytestBDDFramework.bstack1l1llll111l_opy_] = key
        elif test_hook_state == bstack1lll1lll111_opy_.POST:
            bstack1ll1111111l_opy_ = bstack1ll1l111111_opy_.get(key, [])
            hook = bstack1ll1111111l_opy_.pop() if bstack1ll1111111l_opy_ else None
            if hook:
                result = self.__1ll111ll111_opy_(*args)
                if result:
                    bstack1ll11l1l11l_opy_ = result.get(bstack1lllll1l_opy_ (u"ࠨ࡯ࡶࡶࡦࡳࡲ࡫ࠢቑ"), TestFramework.bstack1l1llll1l1l_opy_)
                    if bstack1ll11l1l11l_opy_ != TestFramework.bstack1l1llll1l1l_opy_:
                        hook[TestFramework.bstack1l1llll1l11_opy_] = bstack1ll11l1l11l_opy_
                hook[TestFramework.bstack1ll1111lll1_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll11111l1l_opy_] = bstack1ll1111ll11_opy_.bstack1ll11llllll_opy_()
                self.bstack1ll11ll111l_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll11l11111_opy_, [])
                self.bstack1ll111l1111_opy_(instance, logs)
                bstack1ll1l1l111l_opy_[key].append(hook)
                bstack1ll111ll11l_opy_[PytestBDDFramework.bstack1ll111l1l11_opy_] = key
        TestFramework.bstack1ll1111l11l_opy_(instance, bstack1ll111ll11l_opy_)
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡨࡰࡱ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࡃࡻ࡬ࡧࡼࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢ࡫ࡳࡴࡱࡳࡠࡵࡷࡥࡷࡺࡥࡥ࠿ࡾ࡬ࡴࡵ࡫ࡴࡡࡶࡸࡦࡸࡴࡦࡦࢀࠤ࡭ࡵ࡯࡬ࡵࡢࡪ࡮ࡴࡩࡴࡪࡨࡨࡂࠨቒ") + str(bstack1ll1l1l111l_opy_) + bstack1lllll1l_opy_ (u"ࠣࠤቓ"))
    def __1ll1l11111l_opy_(
        self,
        context: bstack1ll11l11l11_opy_,
        test_framework_state: bstack1llll111l1l_opy_,
        test_hook_state: bstack1lll1lll111_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll11l111ll_opy_(args[0], [bstack1lllll1l_opy_ (u"ࠤࡶࡧࡴࡶࡥࠣቔ"), bstack1lllll1l_opy_ (u"ࠥࡥࡷ࡭࡮ࡢ࡯ࡨࠦቕ"), bstack1lllll1l_opy_ (u"ࠦࡵࡧࡲࡢ࡯ࡶࠦቖ"), bstack1lllll1l_opy_ (u"ࠧ࡯ࡤࡴࠤ቗"), bstack1lllll1l_opy_ (u"ࠨࡵ࡯࡫ࡷࡸࡪࡹࡴࠣቘ"), bstack1lllll1l_opy_ (u"ࠢࡣࡣࡶࡩ࡮ࡪࠢ቙")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scenario = args[2] if len(args) == 3 else None
        scope = request.scope if hasattr(request, bstack1lllll1l_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢቚ")) else fixturedef.get(bstack1lllll1l_opy_ (u"ࠤࡶࡧࡴࡶࡥࠣቛ"), None)
        fixturename = request.fixturename if hasattr(request, bstack1lllll1l_opy_ (u"ࠥࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࠣቜ")) else None
        node = request.node if hasattr(request, bstack1lllll1l_opy_ (u"ࠦࡳࡵࡤࡦࠤቝ")) else None
        target = request.node.nodeid if hasattr(node, bstack1lllll1l_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧ቞")) else None
        baseid = fixturedef.get(bstack1lllll1l_opy_ (u"ࠨࡢࡢࡵࡨ࡭ࡩࠨ቟"), None) or bstack1lllll1l_opy_ (u"ࠢࠣበ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack1lllll1l_opy_ (u"ࠣࡡࡳࡽ࡫ࡻ࡮ࡤ࡫ࡷࡩࡲࠨቡ")):
            target = PytestBDDFramework.__1ll111lll1l_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack1lllll1l_opy_ (u"ࠤ࡯ࡳࡨࡧࡴࡪࡱࡱࠦቢ")) else None
            if target and not TestFramework.bstack1l1llllllll_opy_(target):
                self.__1l1llll1lll_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡩ࡭ࡽࡺࡵࡳࡧࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡪࡦࡲ࡬ࡣࡣࡦ࡯ࠥࡺࡡࡳࡩࡨࡸࡂࢁࡴࡢࡴࡪࡩࡹࢃࠠࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࡂࢁࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࢁࠥࡴ࡯ࡥࡧࡀࡿࡳࡵࡤࡦࡿࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࠧባ") + str(test_hook_state) + bstack1lllll1l_opy_ (u"ࠦࠧቤ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack1lllll1l_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫ࡤࡦࡨࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡩ࡫ࡦࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡷࡥࡷ࡭ࡥࡵ࠿ࠥብ") + str(target) + bstack1lllll1l_opy_ (u"ࠨࠢቦ"))
            return None
        instance = TestFramework.bstack1l1llllllll_opy_(target)
        if not instance:
            self.logger.warning(bstack1lllll1l_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡦࡪࡺࡷࡹࡷ࡫࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰ࡫ࡥࡳࡪ࡬ࡦࡦࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࡃࡻࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡢࡢࡵࡨ࡭ࡩࡃࡻࡣࡣࡶࡩ࡮ࡪࡽࠡࡶࡤࡶ࡬࡫ࡴ࠾ࠤቧ") + str(target) + bstack1lllll1l_opy_ (u"ࠣࠤቨ"))
            return None
        bstack1ll1l11ll11_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll1l111ll1_opy_, {})
        if os.getenv(bstack1lllll1l_opy_ (u"ࠤࡖࡈࡐࡥࡃࡍࡋࡢࡊࡑࡇࡇࡠࡈࡌ࡜࡙࡛ࡒࡆࡕࠥቩ"), bstack1lllll1l_opy_ (u"ࠥ࠵ࠧቪ")) == bstack1lllll1l_opy_ (u"ࠦ࠶ࠨቫ"):
            bstack1l1lllll1l1_opy_ = bstack1lllll1l_opy_ (u"ࠧࡀࠢቬ").join((scope, fixturename))
            bstack1l1lll1ll1l_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll1l1111ll_opy_ = {
                bstack1lllll1l_opy_ (u"ࠨ࡫ࡦࡻࠥቭ"): bstack1l1lllll1l1_opy_,
                bstack1lllll1l_opy_ (u"ࠢࡵࡣࡪࡷࠧቮ"): PytestBDDFramework.__1ll1l1ll111_opy_(request.node, scenario),
                bstack1lllll1l_opy_ (u"ࠣࡨ࡬ࡼࡹࡻࡲࡦࠤቯ"): fixturedef,
                bstack1lllll1l_opy_ (u"ࠤࡶࡧࡴࡶࡥࠣተ"): scope,
                bstack1lllll1l_opy_ (u"ࠥࡸࡾࡶࡥࠣቱ"): None,
            }
            try:
                if test_hook_state == bstack1lll1lll111_opy_.POST and callable(getattr(args[-1], bstack1lllll1l_opy_ (u"ࠦ࡬࡫ࡴࡠࡴࡨࡷࡺࡲࡴࠣቲ"), None)):
                    bstack1ll1l1111ll_opy_[bstack1lllll1l_opy_ (u"ࠧࡺࡹࡱࡧࠥታ")] = TestFramework.bstack1ll11ll1l1l_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll1lll111_opy_.PRE:
                bstack1ll1l1111ll_opy_[bstack1lllll1l_opy_ (u"ࠨࡵࡶ࡫ࡧࠦቴ")] = uuid4().__str__()
                bstack1ll1l1111ll_opy_[PytestBDDFramework.bstack1ll1l11l1l1_opy_] = bstack1l1lll1ll1l_opy_
            elif test_hook_state == bstack1lll1lll111_opy_.POST:
                bstack1ll1l1111ll_opy_[PytestBDDFramework.bstack1ll1111lll1_opy_] = bstack1l1lll1ll1l_opy_
            if bstack1l1lllll1l1_opy_ in bstack1ll1l11ll11_opy_:
                bstack1ll1l11ll11_opy_[bstack1l1lllll1l1_opy_].update(bstack1ll1l1111ll_opy_)
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠢࡶࡲࡧࡥࡹ࡫ࡤࠡࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࡃࡻࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫࠽ࠣት") + str(bstack1ll1l11ll11_opy_[bstack1l1lllll1l1_opy_]) + bstack1lllll1l_opy_ (u"ࠣࠤቶ"))
            else:
                bstack1ll1l11ll11_opy_[bstack1l1lllll1l1_opy_] = bstack1ll1l1111ll_opy_
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠤࡶࡥࡻ࡫ࡤࠡࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࡃࡻࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫࠽ࡼࡶࡨࡷࡹࡥࡦࡪࡺࡷࡹࡷ࡫ࡽࠡࡶࡵࡥࡨࡱࡥࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࡶࡁࠧቷ") + str(len(bstack1ll1l11ll11_opy_)) + bstack1lllll1l_opy_ (u"ࠥࠦቸ"))
        TestFramework.bstack1llll11ll1l_opy_(instance, PytestBDDFramework.bstack1ll1l111ll1_opy_, bstack1ll1l11ll11_opy_)
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠦࡸࡧࡶࡦࡦࠣࡪ࡮ࡾࡴࡶࡴࡨࡷࡂࢁ࡬ࡦࡰࠫࡸࡷࡧࡣ࡬ࡧࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࡸ࠯ࡽࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࠦቹ") + str(instance.ref()) + bstack1lllll1l_opy_ (u"ࠧࠨቺ"))
        return instance
    def __1l1llll1lll_opy_(
        self,
        context: bstack1ll11l11l11_opy_,
        test_framework_state: bstack1llll111l1l_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1ll11ll1_opy_.create_context(target)
        ob = bstack1lll1l1llll_opy_(ctx, self.bstack1ll1l1l11ll_opy_, self.bstack1ll111llll1_opy_, test_framework_state)
        TestFramework.bstack1ll1111l11l_opy_(ob, {
            TestFramework.bstack1lll1l111l1_opy_: context.test_framework_name,
            TestFramework.bstack1lll11lll11_opy_: context.test_framework_version,
            TestFramework.bstack1ll111lllll_opy_: [],
            PytestBDDFramework.bstack1ll1l111ll1_opy_: {},
            PytestBDDFramework.bstack1l1llll1ll1_opy_: {},
            PytestBDDFramework.bstack1ll11l11ll1_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1llll11ll1l_opy_(ob, TestFramework.bstack1ll1111l111_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1llll11ll1l_opy_(ob, TestFramework.bstack1llllllllll_opy_, context.platform_index)
        TestFramework.bstack1lll11lllll_opy_[ctx.id] = ob
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠨࡳࡢࡸࡨࡨࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࠠࡤࡶࡻ࠲࡮ࡪ࠽ࡼࡥࡷࡼ࠳࡯ࡤࡾࠢࡷࡥࡷ࡭ࡥࡵ࠿ࡾࡸࡦࡸࡧࡦࡶࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷࡂࠨቻ") + str(TestFramework.bstack1lll11lllll_opy_.keys()) + bstack1lllll1l_opy_ (u"ࠢࠣቼ"))
        return ob
    @staticmethod
    def __1ll111111ll_opy_(instance, args):
        request, feature, scenario = args
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1lllll1l_opy_ (u"ࠨ࡫ࡧࠫች"): id(step),
                bstack1lllll1l_opy_ (u"ࠩࡷࡩࡽࡺࠧቾ"): step.name,
                bstack1lllll1l_opy_ (u"ࠪ࡯ࡪࡿࡷࡰࡴࡧࠫቿ"): step.keyword,
            })
        meta = {
            bstack1lllll1l_opy_ (u"ࠫ࡫࡫ࡡࡵࡷࡵࡩࠬኀ"): {
                bstack1lllll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪኁ"): feature.name,
                bstack1lllll1l_opy_ (u"࠭ࡰࡢࡶ࡫ࠫኂ"): feature.filename,
                bstack1lllll1l_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬኃ"): feature.description
            },
            bstack1lllll1l_opy_ (u"ࠨࡵࡦࡩࡳࡧࡲࡪࡱࠪኄ"): {
                bstack1lllll1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧኅ"): scenario.name
            },
            bstack1lllll1l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩኆ"): steps,
            bstack1lllll1l_opy_ (u"ࠫࡪࡾࡡ࡮ࡲ࡯ࡩࡸ࠭ኇ"): PytestBDDFramework.__1ll111l1l1l_opy_(request.node)
        }
        instance.data.update(
            {
                TestFramework.bstack1ll1111l1ll_opy_: meta
            }
        )
    def bstack1ll11ll111l_opy_(self, hook: Dict[str, Any]) -> None:
        bstack1lllll1l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡓࡶࡴࡩࡥࡴࡵࡨࡷࠥࡺࡨࡦࠢࡋࡳࡴࡱࡌࡦࡸࡨࡰࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡷ࡮ࡳࡩ࡭ࡣࡵࠤࡹࡵࠠࡵࡪࡨࠤࡏࡧࡶࡢࠢ࡬ࡱࡵࡲࡥ࡮ࡧࡱࡸࡦࡺࡩࡰࡰ࠱ࠎࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡨࡪࡵࠣࡱࡪࡺࡨࡰࡦ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡆ࡬ࡪࡩ࡫ࡴࠢࡷ࡬ࡪࠦࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭ࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥ࡯࡮ࡴ࡫ࡧࡩࠥࢄ࠯࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠯ࡖࡲ࡯ࡳࡦࡪࡥࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡌ࡯ࡳࠢࡨࡥࡨ࡮ࠠࡧ࡫࡯ࡩࠥ࡯࡮ࠡࡪࡲࡳࡰࡥ࡬ࡦࡸࡨࡰࡤ࡬ࡩ࡭ࡧࡶ࠰ࠥࡸࡥࡱ࡮ࡤࡧࡪࡹࠠࠣࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠦࠥࡽࡩࡵࡪࠣࠦࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠢࠡ࡫ࡱࠤ࡮ࡺࡳࠡࡲࡤࡸ࡭࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡏࡦࠡࡣࠣࡪ࡮ࡲࡥࠡ࡫ࡱࠤࡹ࡮ࡥࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡲࡧࡴࡤࡪࡨࡷࠥࡧࠠ࡮ࡱࡧ࡭࡫࡯ࡥࡥࠢ࡫ࡳࡴࡱ࠭࡭ࡧࡹࡩࡱࠦࡦࡪ࡮ࡨ࠰ࠥ࡯ࡴࠡࡥࡵࡩࡦࡺࡥࡴࠢࡤࠤࡑࡵࡧࡆࡰࡷࡶࡾࠦ࡯ࡣ࡬ࡨࡧࡹࠦࡷࡪࡶ࡫ࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࠡࡦࡨࡸࡦ࡯࡬ࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡕ࡬ࡱ࡮ࡲࡡࡳ࡮ࡼ࠰ࠥ࡯ࡴࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦ࡬ࡰࡥࡤࡸࡪࡪࠠࡪࡰࠣࡌࡴࡵ࡫ࡍࡧࡹࡩࡱ࠵ࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠥࡨࡹࠡࡴࡨࡴࡱࡧࡣࡪࡰࡪࠤࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤࠣࡻ࡮ࡺࡨࠡࠤࡋࡳࡴࡱࡌࡦࡸࡨࡰ࠴ࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠦ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤ࡙࡮ࡥࠡࡥࡵࡩࡦࡺࡥࡥࠢࡏࡳ࡬ࡋ࡮ࡵࡴࡼࠤࡴࡨࡪࡦࡥࡷࡷࠥࡧࡲࡦࠢࡤࡨࡩ࡫ࡤࠡࡶࡲࠤࡹ࡮ࡥࠡࡪࡲࡳࡰ࠭ࡳࠡࠤ࡯ࡳ࡬ࡹࠢࠡ࡮࡬ࡷࡹ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡃࡵ࡫ࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡮࡯ࡰ࡭࠽ࠤ࡙࡮ࡥࠡࡧࡹࡩࡳࡺࠠࡥ࡫ࡦࡸ࡮ࡵ࡮ࡢࡴࡼࠤࡨࡵ࡮ࡵࡣ࡬ࡲ࡮ࡴࡧࠡࡧࡻ࡭ࡸࡺࡩ࡯ࡩࠣࡰࡴ࡭ࡳࠡࡣࡱࡨࠥ࡮࡯ࡰ࡭ࠣ࡭ࡳ࡬࡯ࡳ࡯ࡤࡸ࡮ࡵ࡮࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡩࡱࡲ࡯ࡤࡲࡥࡷࡧ࡯ࡣ࡫࡯࡬ࡦࡵ࠽ࠤࡑ࡯ࡳࡵࠢࡲࡪࠥࡖࡡࡵࡪࠣࡳࡧࡰࡥࡤࡶࡶࠤ࡫ࡸ࡯࡮ࠢࡷ࡬ࡪࠦࡔࡦࡵࡷࡐࡪࡼࡥ࡭ࠢࡰࡳࡳ࡯ࡴࡰࡴ࡬ࡲ࡬࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡨࡵࡪ࡮ࡧࡣࡱ࡫ࡶࡦ࡮ࡢࡪ࡮ࡲࡥࡴ࠼ࠣࡐ࡮ࡹࡴࠡࡱࡩࠤࡕࡧࡴࡩࠢࡲࡦ࡯࡫ࡣࡵࡵࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩࠥࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠢࡰࡳࡳ࡯ࡴࡰࡴ࡬ࡲ࡬࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦኈ")
        global _1ll111l11l1_opy_
        platform_index = os.environ[bstack1lllll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭኉")]
        bstack1ll1l11l11l_opy_ = os.path.join(bstack1ll11ll1111_opy_, (bstack1ll11lll11l_opy_ + str(platform_index)), bstack1ll11lll1l1_opy_)
        if not os.path.exists(bstack1ll1l11l11l_opy_) or not os.path.isdir(bstack1ll1l11l11l_opy_):
            return
        logs = hook.get(bstack1lllll1l_opy_ (u"ࠢ࡭ࡱࡪࡷࠧኊ"), [])
        with os.scandir(bstack1ll1l11l11l_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll111l11l1_opy_:
                    self.logger.info(bstack1lllll1l_opy_ (u"ࠣࡒࡤࡸ࡭ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡱࡴࡲࡧࡪࡹࡳࡦࡦࠣࡿࢂࠨኋ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack1lllll1l_opy_ (u"ࠤࠥኌ")
                    log_entry = bstack1ll1l1l1ll1_opy_(
                        kind=bstack1lllll1l_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧኍ"),
                        message=bstack1lllll1l_opy_ (u"ࠦࠧ኎"),
                        level=bstack1lllll1l_opy_ (u"ࠧࠨ኏"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1ll11l1l111_opy_=entry.stat().st_size,
                        bstack1ll1l1l11l1_opy_=bstack1lllll1l_opy_ (u"ࠨࡍࡂࡐࡘࡅࡑࡥࡕࡑࡎࡒࡅࡉࠨነ"),
                        bstack111l1l1_opy_=os.path.abspath(entry.path),
                        bstack1ll11111l11_opy_=hook.get(TestFramework.bstack1ll11l1ll1l_opy_)
                    )
                    logs.append(log_entry)
                    _1ll111l11l1_opy_.add(abs_path)
        platform_index = os.environ[bstack1lllll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧኑ")]
        bstack1ll1l1111l1_opy_ = os.path.join(bstack1ll11ll1111_opy_, (bstack1ll11lll11l_opy_ + str(platform_index)), bstack1ll11lll1l1_opy_, bstack1l1llll1111_opy_)
        if not os.path.exists(bstack1ll1l1111l1_opy_) or not os.path.isdir(bstack1ll1l1111l1_opy_):
            self.logger.info(bstack1lllll1l_opy_ (u"ࠣࡐࡲࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤ࡫ࡵࡵ࡯ࡦࠣࡥࡹࡀࠠࡼࡿࠥኒ").format(bstack1ll1l1111l1_opy_))
        else:
            self.logger.info(bstack1lllll1l_opy_ (u"ࠤࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡪࡷࡵ࡭ࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼ࠾ࠥࢁࡽࠣና").format(bstack1ll1l1111l1_opy_))
            with os.scandir(bstack1ll1l1111l1_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll111l11l1_opy_:
                        self.logger.info(bstack1lllll1l_opy_ (u"ࠥࡔࡦࡺࡨࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡳࡶࡴࡩࡥࡴࡵࡨࡨࠥࢁࡽࠣኔ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack1lllll1l_opy_ (u"ࠦࠧን")
                        log_entry = bstack1ll1l1l1ll1_opy_(
                            kind=bstack1lllll1l_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢኖ"),
                            message=bstack1lllll1l_opy_ (u"ࠨࠢኗ"),
                            level=bstack1lllll1l_opy_ (u"ࠢࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠦኘ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1ll11l1l111_opy_=entry.stat().st_size,
                            bstack1ll1l1l11l1_opy_=bstack1lllll1l_opy_ (u"ࠣࡏࡄࡒ࡚ࡇࡌࡠࡗࡓࡐࡔࡇࡄࠣኙ"),
                            bstack111l1l1_opy_=os.path.abspath(entry.path),
                            bstack1l1lllllll1_opy_=hook.get(TestFramework.bstack1ll11l1ll1l_opy_)
                        )
                        logs.append(log_entry)
                        _1ll111l11l1_opy_.add(abs_path)
        hook[bstack1lllll1l_opy_ (u"ࠤ࡯ࡳ࡬ࡹࠢኚ")] = logs
    def bstack1ll111l1111_opy_(
        self,
        bstack1ll11ll11ll_opy_: bstack1lll1l1llll_opy_,
        entries: List[bstack1ll1l1l1ll1_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack1lllll1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡗࡊ࡙ࡓࡊࡑࡑࡣࡎࡊࠢኛ"))
        req.platform_index = TestFramework.get_state(bstack1ll11ll11ll_opy_, TestFramework.bstack1llllllllll_opy_)
        req.execution_context.hash = str(bstack1ll11ll11ll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll11ll11ll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll11ll11ll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll11ll11ll_opy_, TestFramework.bstack1lll1l111l1_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll11ll11ll_opy_, TestFramework.bstack1lll11lll11_opy_)
            log_entry.uuid = entry.bstack1ll11111l11_opy_ if entry.bstack1ll11111l11_opy_ else TestFramework.get_state(bstack1ll11ll11ll_opy_, TestFramework.bstack1lll1lll1ll_opy_)
            log_entry.test_framework_state = bstack1ll11ll11ll_opy_.state.name
            log_entry.message = entry.message.encode(bstack1lllll1l_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥኜ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack1lllll1l_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢኝ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll11l1l111_opy_
                log_entry.file_path = entry.bstack111l1l1_opy_
        def bstack1ll111lll11_opy_():
            bstack1ll111ll1_opy_ = datetime.now()
            try:
                self.bstack1lllllll111_opy_.LogCreatedEvent(req)
                bstack1ll11ll11ll_opy_.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡ࡯ࡳ࡬ࡥࡣࡳࡧࡤࡸࡪࡪ࡟ࡦࡸࡨࡲࡹࡥࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠥኞ"), datetime.now() - bstack1ll111ll1_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1lllll1l_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࡸ࡫࡮ࡥࡡ࡯ࡳ࡬ࡥࡣࡳࡧࡤࡸࡪࡪ࡟ࡦࡸࡨࡲࡹࡥࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠣࡿࢂࠨኟ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11l1l11_opy_.enqueue(bstack1ll111lll11_opy_)
    def __1ll1l1l1111_opy_(self, instance) -> None:
        bstack1lllll1l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡒ࡯ࡢࡦࡶࠤࡨࡻࡳࡵࡱࡰࠤࡹࡧࡧࡴࠢࡩࡳࡷࠦࡴࡩࡧࠣ࡫࡮ࡼࡥ࡯ࠢࡷࡩࡸࡺࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡄࡴࡨࡥࡹ࡫ࡳࠡࡣࠣࡨ࡮ࡩࡴࠡࡥࡲࡲࡹࡧࡩ࡯࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡰࡪࡼࡥ࡭ࠢࡦࡹࡸࡺ࡯࡮ࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࡪࠠࡧࡴࡲࡱࠏࠦࠠࠡࠢࠣࠤࠥࠦࡃࡶࡵࡷࡳࡲ࡚ࡡࡨࡏࡤࡲࡦ࡭ࡥࡳࠢࡤࡲࡩࠦࡵࡱࡦࡤࡸࡪࡹࠠࡵࡪࡨࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࠦࡳࡵࡣࡷࡩࠥࡻࡳࡪࡰࡪࠤࡸ࡫ࡴࡠࡵࡷࡥࡹ࡫࡟ࡦࡰࡷࡶ࡮࡫ࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨአ")
        bstack1ll111ll11l_opy_ = {bstack1lllll1l_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡡࡰࡩࡹࡧࡤࡢࡶࡤࠦኡ"): bstack1ll1111ll11_opy_.bstack1ll11llllll_opy_()}
        TestFramework.bstack1ll1111l11l_opy_(instance, bstack1ll111ll11l_opy_)
    @staticmethod
    def __1ll11ll1lll_opy_(instance, args):
        request, bstack1l1lll1ll11_opy_ = args
        bstack1ll11l1l1ll_opy_ = id(bstack1l1lll1ll11_opy_)
        bstack1ll11ll1l11_opy_ = instance.data[TestFramework.bstack1ll1111l1ll_opy_]
        step = next(filter(lambda st: st[bstack1lllll1l_opy_ (u"ࠪ࡭ࡩ࠭ኢ")] == bstack1ll11l1l1ll_opy_, bstack1ll11ll1l11_opy_[bstack1lllll1l_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪኣ")]), None)
        step.update({
            bstack1lllll1l_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩኤ"): datetime.now(tz=timezone.utc)
        })
        index = next((i for i, st in enumerate(bstack1ll11ll1l11_opy_[bstack1lllll1l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬእ")]) if st[bstack1lllll1l_opy_ (u"ࠧࡪࡦࠪኦ")] == step[bstack1lllll1l_opy_ (u"ࠨ࡫ࡧࠫኧ")]), None)
        if index is not None:
            bstack1ll11ll1l11_opy_[bstack1lllll1l_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨከ")][index] = step
        instance.data[TestFramework.bstack1ll1111l1ll_opy_] = bstack1ll11ll1l11_opy_
    @staticmethod
    def __1ll11l1ll11_opy_(instance, args):
        bstack1lllll1l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡸࡪࡨࡲࠥࡲࡥ࡯ࠢࡤࡶ࡬ࡹࠠࡪࡵࠣ࠶࠱ࠦࡩࡵࠢࡶ࡭࡬ࡴࡩࡧ࡫ࡨࡷࠥࡺࡨࡦࡴࡨࠤ࡮ࡹࠠ࡯ࡱࠣࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡦࡸࡧࡴࠢࡤࡶࡪࠦ࠭ࠡ࡝ࡵࡩࡶࡻࡥࡴࡶ࠯ࠤࡸࡺࡥࡱ࡟ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡮࡬ࠠࡢࡴࡪࡷࠥࡧࡲࡦࠢ࠶ࠤࡹ࡮ࡥ࡯ࠢࡷ࡬ࡪࠦ࡬ࡢࡵࡷࠤࡻࡧ࡬ࡶࡧࠣ࡭ࡸࠦࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨኩ")
        bstack1ll1l11ll1l_opy_ = datetime.now(tz=timezone.utc)
        request = args[0]
        bstack1l1lll1ll11_opy_ = args[1]
        bstack1ll11l1l1ll_opy_ = id(bstack1l1lll1ll11_opy_)
        bstack1ll11ll1l11_opy_ = instance.data[TestFramework.bstack1ll1111l1ll_opy_]
        step = None
        if bstack1ll11l1l1ll_opy_ is not None and bstack1ll11ll1l11_opy_.get(bstack1lllll1l_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪኪ")):
            step = next(filter(lambda st: st[bstack1lllll1l_opy_ (u"ࠬ࡯ࡤࠨካ")] == bstack1ll11l1l1ll_opy_, bstack1ll11ll1l11_opy_[bstack1lllll1l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬኬ")]), None)
            step.update({
                bstack1lllll1l_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬክ"): bstack1ll1l11ll1l_opy_,
            })
        if len(args) > 2:
            exception = args[2]
            step.update({
                bstack1lllll1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨኮ"): bstack1lllll1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩኯ"),
                bstack1lllll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫኰ"): str(exception)
            })
        else:
            if step is not None:
                step.update({
                    bstack1lllll1l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ኱"): bstack1lllll1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬኲ"),
                })
        index = next((i for i, st in enumerate(bstack1ll11ll1l11_opy_[bstack1lllll1l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬኳ")]) if st[bstack1lllll1l_opy_ (u"ࠧࡪࡦࠪኴ")] == step[bstack1lllll1l_opy_ (u"ࠨ࡫ࡧࠫኵ")]), None)
        if index is not None:
            bstack1ll11ll1l11_opy_[bstack1lllll1l_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨ኶")][index] = step
        instance.data[TestFramework.bstack1ll1111l1ll_opy_] = bstack1ll11ll1l11_opy_
    @staticmethod
    def __1ll111l1l1l_opy_(node):
        try:
            examples = []
            if hasattr(node, bstack1lllll1l_opy_ (u"ࠪࡧࡦࡲ࡬ࡴࡲࡨࡧࠬ኷")):
                examples = list(node.callspec.params[bstack1lllll1l_opy_ (u"ࠫࡤࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡨࡼࡦࡳࡰ࡭ࡧࠪኸ")].values())
            return examples
        except:
            return []
    def bstack1ll11ll1ll1_opy_(self, instance: bstack1lll1l1llll_opy_, bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_]):
        bstack1ll11111lll_opy_ = (
            PytestBDDFramework.bstack1l1llll111l_opy_
            if bstack1llll1l1lll_opy_[1] == bstack1lll1lll111_opy_.PRE
            else PytestBDDFramework.bstack1ll111l1l11_opy_
        )
        hook = PytestBDDFramework.bstack1l1lllll111_opy_(instance, bstack1ll11111lll_opy_)
        entries = hook.get(TestFramework.bstack1ll111ll1ll_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll111lllll_opy_, []))
        return entries
    def bstack1l1llll11l1_opy_(self, instance: bstack1lll1l1llll_opy_, bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_]):
        bstack1ll11111lll_opy_ = (
            PytestBDDFramework.bstack1l1llll111l_opy_
            if bstack1llll1l1lll_opy_[1] == bstack1lll1lll111_opy_.PRE
            else PytestBDDFramework.bstack1ll111l1l11_opy_
        )
        PytestBDDFramework.bstack1l1llllll1l_opy_(instance, bstack1ll11111lll_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll111lllll_opy_, []).clear()
    @staticmethod
    def bstack1l1lllll111_opy_(instance: bstack1lll1l1llll_opy_, bstack1ll11111lll_opy_: str):
        bstack1ll1l11l111_opy_ = (
            PytestBDDFramework.bstack1l1llll1ll1_opy_
            if bstack1ll11111lll_opy_ == PytestBDDFramework.bstack1ll111l1l11_opy_
            else PytestBDDFramework.bstack1ll11l11ll1_opy_
        )
        bstack1ll11111ll1_opy_ = TestFramework.get_state(instance, bstack1ll11111lll_opy_, None)
        bstack1l1lllll11l_opy_ = TestFramework.get_state(instance, bstack1ll1l11l111_opy_, None) if bstack1ll11111ll1_opy_ else None
        return (
            bstack1l1lllll11l_opy_[bstack1ll11111ll1_opy_][-1]
            if isinstance(bstack1l1lllll11l_opy_, dict) and len(bstack1l1lllll11l_opy_.get(bstack1ll11111ll1_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1l1llllll1l_opy_(instance: bstack1lll1l1llll_opy_, bstack1ll11111lll_opy_: str):
        hook = PytestBDDFramework.bstack1l1lllll111_opy_(instance, bstack1ll11111lll_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll111ll1ll_opy_, []).clear()
    @staticmethod
    def __1ll111l1ll1_opy_(instance: bstack1lll1l1llll_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack1lllll1l_opy_ (u"ࠧ࡭ࡥࡵࡡࡵࡩࡨࡵࡲࡥࡵࠥኹ"), None)):
            return
        if os.getenv(bstack1lllll1l_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡇࡎࡄࡋࡤࡒࡏࡈࡕࠥኺ"), bstack1lllll1l_opy_ (u"ࠢ࠲ࠤኻ")) != bstack1lllll1l_opy_ (u"ࠣ࠳ࠥኼ"):
            PytestBDDFramework.logger.warning(bstack1lllll1l_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡪࡰࡪࠤࡨࡧࡰ࡭ࡱࡪࠦኽ"))
            return
        bstack1ll1111ll1l_opy_ = {
            bstack1lllll1l_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤኾ"): (PytestBDDFramework.bstack1l1llll111l_opy_, PytestBDDFramework.bstack1ll11l11ll1_opy_),
            bstack1lllll1l_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨ኿"): (PytestBDDFramework.bstack1ll111l1l11_opy_, PytestBDDFramework.bstack1l1llll1ll1_opy_),
        }
        for when in (bstack1lllll1l_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦዀ"), bstack1lllll1l_opy_ (u"ࠨࡣࡢ࡮࡯ࠦ዁"), bstack1lllll1l_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤዂ")):
            bstack1ll1l1ll1l1_opy_ = args[1].get_records(when)
            if not bstack1ll1l1ll1l1_opy_:
                continue
            records = [
                bstack1ll1l1l1ll1_opy_(
                    kind=TestFramework.bstack1ll1l111l1l_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack1lllll1l_opy_ (u"ࠣ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨࠦዃ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack1lllll1l_opy_ (u"ࠤࡦࡶࡪࡧࡴࡦࡦࠥዄ")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll1l1ll1l1_opy_
                if isinstance(getattr(r, bstack1lllll1l_opy_ (u"ࠥࡱࡪࡹࡳࡢࡩࡨࠦዅ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll1l111l11_opy_, bstack1ll1l11l111_opy_ = bstack1ll1111ll1l_opy_.get(when, (None, None))
            bstack1ll11lll1ll_opy_ = TestFramework.get_state(instance, bstack1ll1l111l11_opy_, None) if bstack1ll1l111l11_opy_ else None
            bstack1l1lllll11l_opy_ = TestFramework.get_state(instance, bstack1ll1l11l111_opy_, None) if bstack1ll11lll1ll_opy_ else None
            if isinstance(bstack1l1lllll11l_opy_, dict) and len(bstack1l1lllll11l_opy_.get(bstack1ll11lll1ll_opy_, [])) > 0:
                hook = bstack1l1lllll11l_opy_[bstack1ll11lll1ll_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll111ll1ll_opy_ in hook:
                    hook[TestFramework.bstack1ll111ll1ll_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll111lllll_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll11lllll1_opy_(args) -> Dict[str, Any]:
        request, feature, scenario = args
        test_id = request.node.nodeid
        test_name = PytestBDDFramework.__1ll1l1l1l11_opy_(request.node, scenario)
        bstack1ll111l1lll_opy_ = feature.filename
        if not test_id or not test_name or not bstack1ll111l1lll_opy_:
            return None
        code = None
        return {
            TestFramework.bstack1lll1lll1ll_opy_: uuid4().__str__(),
            TestFramework.bstack1ll1l11lll1_opy_: test_id,
            TestFramework.bstack1ll111l111l_opy_: test_name,
            TestFramework.bstack1ll11l1l1l1_opy_: test_id,
            TestFramework.bstack1ll11l11lll_opy_: bstack1ll111l1lll_opy_,
            TestFramework.bstack1ll11l1111l_opy_: PytestBDDFramework.__1ll1l1ll111_opy_(feature, scenario),
            TestFramework.bstack1ll1111llll_opy_: code,
            TestFramework.bstack1lll1l1111l_opy_: TestFramework.bstack1l1llllll11_opy_,
            TestFramework.bstack1lll111l11l_opy_: test_name
        }
    @staticmethod
    def __1ll1l1l1l11_opy_(node, scenario):
        if hasattr(node, bstack1lllll1l_opy_ (u"ࠫࡨࡧ࡬࡭ࡵࡳࡩࡨ࠭዆")):
            parts = node.nodeid.rsplit(bstack1lllll1l_opy_ (u"ࠧࡡࠢ዇"))
            params = parts[-1]
            return bstack1lllll1l_opy_ (u"ࠨࡻࡾࠢ࡞ࡿࢂࠨወ").format(scenario.name, params)
        return scenario.name
    @staticmethod
    def __1ll1l1ll111_opy_(feature, scenario) -> List[str]:
        return (list(feature.tags) if hasattr(feature, bstack1lllll1l_opy_ (u"ࠧࡵࡣࡪࡷࠬዉ")) else []) + (list(scenario.tags) if hasattr(scenario, bstack1lllll1l_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭ዊ")) else [])
    @staticmethod
    def __1ll111lll1l_opy_(location):
        return bstack1lllll1l_opy_ (u"ࠤ࠽࠾ࠧዋ").join(filter(lambda x: isinstance(x, str), location))