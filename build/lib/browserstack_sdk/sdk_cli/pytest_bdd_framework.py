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
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1lll1111111_opy_ import bstack1ll1ll1ll11_opy_
from browserstack_sdk.sdk_cli.utils.bstack1111l11lll_opy_ import bstack1ll11l1l111_opy_
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1lll1ll111l_opy_,
    bstack1lll1l11l11_opy_,
    bstack1lll1l1ll11_opy_,
    bstack1ll11111l1l_opy_,
    bstack1ll1l11ll1l_opy_,
)
import traceback
from bstack_utils.helper import bstack1ll11ll111l_opy_
from bstack_utils.bstack11l1ll11l_opy_ import bstack111111l11l_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.utils.bstack1ll11lll1l1_opy_ import bstack1l1lllll111_opy_
from browserstack_sdk.sdk_cli.bstack1lll11lll1l_opy_ import bstack1lll11llll1_opy_
bstack1ll11l1l1l1_opy_ = bstack1ll11ll111l_opy_()
bstack1ll1l1ll1ll_opy_ = bstack11111_opy_ (u"ࠨࡕࡱ࡮ࡲࡥࡩ࡫ࡤࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷ࠲ࠨᇨ")
bstack1ll1111111l_opy_ = bstack11111_opy_ (u"ࠢࡉࡱࡲ࡯ࡑ࡫ࡶࡦ࡮ࠥᇩ")
bstack1ll11l11ll1_opy_ = bstack11111_opy_ (u"ࠣࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࡍࡵ࡯࡬ࡇࡹࡩࡳࡺࠢᇪ")
bstack1ll1l1l11l1_opy_ = 1.0
_1ll1111lll1_opy_ = set()
class PytestBDDFramework(TestFramework):
    bstack1l1llll1ll1_opy_ = bstack11111_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴࠤᇫ")
    bstack1ll1l11l1ll_opy_ = bstack11111_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡹ࡟ࡴࡶࡤࡶࡹ࡫ࡤࠣᇬ")
    bstack1ll1l1l1lll_opy_ = bstack11111_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱࡳࡠࡨ࡬ࡲ࡮ࡹࡨࡦࡦࠥᇭ")
    bstack1ll1l111ll1_opy_ = bstack11111_opy_ (u"ࠧࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠ࡮ࡤࡷࡹࡥࡳࡵࡣࡵࡸࡪࡪࠢᇮ")
    bstack1ll11l111ll_opy_ = bstack11111_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡ࡯ࡥࡸࡺ࡟ࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࠤᇯ")
    bstack1ll1l11lll1_opy_: bool
    bstack1lll11lll1l_opy_: bstack1lll11llll1_opy_  = None
    bstack1ll1l1l1l11_opy_ = [
        bstack1lll1ll111l_opy_.BEFORE_ALL,
        bstack1lll1ll111l_opy_.AFTER_ALL,
        bstack1lll1ll111l_opy_.BEFORE_EACH,
        bstack1lll1ll111l_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll11lll11l_opy_: Dict[str, str],
        bstack1ll111llll1_opy_: List[str]=[bstack11111_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠦᇰ")],
        bstack1lll11lll1l_opy_: bstack1lll11llll1_opy_ = None,
        bstack1llll1lll11_opy_=None
    ):
        super().__init__(bstack1ll111llll1_opy_, bstack1ll11lll11l_opy_, bstack1lll11lll1l_opy_)
        self.bstack1ll1l11lll1_opy_ = any(bstack11111_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠧᇱ") in item.lower() for item in bstack1ll111llll1_opy_)
        self.bstack1llll1lll11_opy_ = bstack1llll1lll11_opy_
    def track_event(
        self,
        context: bstack1ll11111l1l_opy_,
        test_framework_state: bstack1lll1ll111l_opy_,
        test_hook_state: bstack1lll1l1ll11_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1lll1ll111l_opy_.TEST or test_framework_state in PytestBDDFramework.bstack1ll1l1l1l11_opy_:
            bstack1ll11l1l111_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1lll1ll111l_opy_.NONE:
            self.logger.warning(bstack11111_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡦࡦࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯ࠥࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦ࠿ࠥᇲ") + str(test_hook_state) + bstack11111_opy_ (u"ࠥࠦᇳ"))
            return
        if not self.bstack1ll1l11lll1_opy_:
            self.logger.warning(bstack11111_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳࡹࡵࡱࡲࡲࡶࡹ࡫ࡤࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡁࠧᇴ") + str(str(self.bstack1ll111llll1_opy_)) + bstack11111_opy_ (u"ࠧࠨᇵ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack11111_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡦࡺࡳࡩࡨࡺࡥࡥࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᇶ") + str(kwargs) + bstack11111_opy_ (u"ࠢࠣᇷ"))
            return
        instance = self.__1l1lllll11l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack11111_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰ࡫ࡥࡳࡪ࡬ࡦࡦࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡣࡵ࡫ࡸࡃࠢᇸ") + str(args) + bstack11111_opy_ (u"ࠤࠥᇹ"))
            return
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll1l1l1l11_opy_ and test_hook_state == bstack1lll1l1ll11_opy_.PRE:
                bstack1l1lllll1ll_opy_ = bstack111111l11l_opy_.bstack1ll1l11l1l1_opy_(EVENTS.bstack111l1l1ll1_opy_.value)
                name = str(EVENTS.bstack111l1l1ll1_opy_.name)+bstack11111_opy_ (u"ࠥ࠾ࠧᇺ")+str(test_framework_state.name)
                TestFramework.bstack1ll11111lll_opy_(instance, name, bstack1l1lllll1ll_opy_)
        except Exception as e:
            self.logger.debug(bstack11111_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣ࡬ࡴࡵ࡫ࠡࡧࡵࡶࡴࡸࠠࡱࡴࡨ࠾ࠥࢁࡽࠣᇻ").format(e))
        try:
            if test_framework_state == bstack1lll1ll111l_opy_.TEST:
                if not TestFramework.bstack1llllllll1l_opy_(instance, TestFramework.bstack1ll11l1111l_opy_) and test_hook_state == bstack1lll1l1ll11_opy_.PRE:
                    if not (len(args) >= 3):
                        return
                    test = PytestBDDFramework.__1l1lllll1l1_opy_(args)
                    if test:
                        instance.data.update(test)
                        self.logger.debug(bstack11111_opy_ (u"ࠧࡲ࡯ࡢࡦࡨࡨࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡶࡪ࡬ࠨࠪࡿࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࠧᇼ") + str(test_hook_state) + bstack11111_opy_ (u"ࠨࠢᇽ"))
                if test_hook_state == bstack1lll1l1ll11_opy_.PRE and not TestFramework.bstack1llllllll1l_opy_(instance, TestFramework.bstack1ll111ll11l_opy_):
                    TestFramework.bstack11111111ll_opy_(instance, TestFramework.bstack1ll111ll11l_opy_, datetime.now(tz=timezone.utc))
                    PytestBDDFramework.__1ll1l111111_opy_(instance, args)
                    self.logger.debug(bstack11111_opy_ (u"ࠢࡴࡧࡷࠤࡹ࡫ࡳࡵ࠯ࡶࡸࡦࡸࡴࠡࡨࡲࡶࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡶࡪ࡬ࠨࠪࡿࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࠧᇾ") + str(test_hook_state) + bstack11111_opy_ (u"ࠣࠤᇿ"))
                elif test_hook_state == bstack1lll1l1ll11_opy_.POST and not TestFramework.bstack1llllllll1l_opy_(instance, TestFramework.bstack1ll1l1l1ll1_opy_):
                    TestFramework.bstack11111111ll_opy_(instance, TestFramework.bstack1ll1l1l1ll1_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack11111_opy_ (u"ࠤࡶࡩࡹࠦࡴࡦࡵࡷ࠱ࡪࡴࡤࠡࡨࡲࡶࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡶࡪ࡬ࠨࠪࡿࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࠧሀ") + str(test_hook_state) + bstack11111_opy_ (u"ࠥࠦሁ"))
            elif test_framework_state == bstack1lll1ll111l_opy_.STEP:
                if test_hook_state == bstack1lll1l1ll11_opy_.PRE:
                    PytestBDDFramework.__1ll111l1111_opy_(instance, args)
                elif test_hook_state == bstack1lll1l1ll11_opy_.POST:
                    PytestBDDFramework.__1ll1l1lllll_opy_(instance, args)
            elif test_framework_state == bstack1lll1ll111l_opy_.LOG and test_hook_state == bstack1lll1l1ll11_opy_.POST:
                PytestBDDFramework.__1ll1l111lll_opy_(instance, *args)
            elif test_framework_state == bstack1lll1ll111l_opy_.LOG_REPORT and test_hook_state == bstack1lll1l1ll11_opy_.POST:
                self.__1ll11l11111_opy_(instance, *args)
                self.__1ll1l11l11l_opy_(instance)
            elif test_framework_state in PytestBDDFramework.bstack1ll1l1l1l11_opy_:
                self.__1ll111lllll_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack11111_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣ࡬ࡦࡴࡤ࡭ࡧࡧࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࠧሂ") + str(instance.ref()) + bstack11111_opy_ (u"ࠧࠨሃ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll111l11ll_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll1l1l1l11_opy_ and test_hook_state == bstack1lll1l1ll11_opy_.POST:
                name = str(EVENTS.bstack111l1l1ll1_opy_.name)+bstack11111_opy_ (u"ࠨ࠺ࠣሄ")+str(test_framework_state.name)
                bstack1l1lllll1ll_opy_ = TestFramework.bstack1ll11lll111_opy_(instance, name)
                bstack111111l11l_opy_.end(EVENTS.bstack111l1l1ll1_opy_.value, bstack1l1lllll1ll_opy_+bstack11111_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢህ"), bstack1l1lllll1ll_opy_+bstack11111_opy_ (u"ࠣ࠼ࡨࡲࡩࠨሆ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack11111_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡪࡲࡳࡰࠦࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠤሇ").format(e))
    def bstack1ll11111l11_opy_(self):
        return self.bstack1ll1l11lll1_opy_
    def __1ll1111l111_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack11111_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡳࡧࡶࡹࡱࡺࠢለ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll111l1lll_opy_(rep, [bstack11111_opy_ (u"ࠦࡼ࡮ࡥ࡯ࠤሉ"), bstack11111_opy_ (u"ࠧࡵࡵࡵࡥࡲࡱࡪࠨሊ"), bstack11111_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨላ"), bstack11111_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢሌ"), bstack11111_opy_ (u"ࠣࡵ࡮࡭ࡵࡶࡥࡥࠤል"), bstack11111_opy_ (u"ࠤ࡯ࡳࡳ࡭ࡲࡦࡲࡵࡸࡪࡾࡴࠣሎ")])
        return None
    def __1ll11l11111_opy_(self, instance: bstack1lll1l11l11_opy_, *args):
        result = self.__1ll1111l111_opy_(*args)
        if not result:
            return
        failure = None
        bstack111111lll1_opy_ = None
        if result.get(bstack11111_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦሏ"), None) == bstack11111_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦሐ") and len(args) > 1 and getattr(args[1], bstack11111_opy_ (u"ࠧ࡫ࡸࡤ࡫ࡱࡪࡴࠨሑ"), None) is not None:
            failure = [{bstack11111_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩሒ"): [args[1].excinfo.exconly(), result.get(bstack11111_opy_ (u"ࠢ࡭ࡱࡱ࡫ࡷ࡫ࡰࡳࡶࡨࡼࡹࠨሓ"), None)]}]
            bstack111111lll1_opy_ = bstack11111_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤሔ") if bstack11111_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧሕ") in getattr(args[1].excinfo, bstack11111_opy_ (u"ࠥࡸࡾࡶࡥ࡯ࡣࡰࡩࠧሖ"), bstack11111_opy_ (u"ࠦࠧሗ")) else bstack11111_opy_ (u"࡛ࠧ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࠨመ")
        bstack1ll1111ll1l_opy_ = result.get(bstack11111_opy_ (u"ࠨ࡯ࡶࡶࡦࡳࡲ࡫ࠢሙ"), TestFramework.bstack1ll11ll1111_opy_)
        if bstack1ll1111ll1l_opy_ != TestFramework.bstack1ll11ll1111_opy_:
            TestFramework.bstack11111111ll_opy_(instance, TestFramework.bstack1ll111lll1l_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll11l1llll_opy_(instance, {
            TestFramework.bstack1llll111111_opy_: failure,
            TestFramework.bstack1ll111111l1_opy_: bstack111111lll1_opy_,
            TestFramework.bstack1llll11l1l1_opy_: bstack1ll1111ll1l_opy_,
        })
    def __1l1lllll11l_opy_(
        self,
        context: bstack1ll11111l1l_opy_,
        test_framework_state: bstack1lll1ll111l_opy_,
        test_hook_state: bstack1lll1l1ll11_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1lll1ll111l_opy_.SETUP_FIXTURE:
            instance = self.__1ll111l1l1l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll1l11111l_opy_ bstack1ll1l1111l1_opy_ this to be bstack11111_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢሚ")
            if test_framework_state == bstack1lll1ll111l_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll1l11ll11_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1lll1ll111l_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack11111_opy_ (u"ࠣࡰࡲࡨࡪࠨማ"), None), bstack11111_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤሜ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack11111_opy_ (u"ࠥࡲࡴࡪࡥࠣም"), None):
                target = args[0].node.nodeid
            elif getattr(args[0], bstack11111_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦሞ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll1ll1111l_opy_(target) if target else None
        return instance
    def __1ll111lllll_opy_(
        self,
        instance: bstack1lll1l11l11_opy_,
        test_framework_state: bstack1lll1ll111l_opy_,
        test_hook_state: bstack1lll1l1ll11_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll11111111_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll1l11l1ll_opy_, {})
        if not key in bstack1ll11111111_opy_:
            bstack1ll11111111_opy_[key] = []
        bstack1ll11ll1lll_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll1l1l1lll_opy_, {})
        if not key in bstack1ll11ll1lll_opy_:
            bstack1ll11ll1lll_opy_[key] = []
        bstack1ll111ll1ll_opy_ = {
            PytestBDDFramework.bstack1ll1l11l1ll_opy_: bstack1ll11111111_opy_,
            PytestBDDFramework.bstack1ll1l1l1lll_opy_: bstack1ll11ll1lll_opy_,
        }
        if test_hook_state == bstack1lll1l1ll11_opy_.PRE:
            hook_name = args[1] if len(args) > 1 else None
            hook = {
                bstack11111_opy_ (u"ࠧࡱࡥࡺࠤሟ"): key,
                TestFramework.bstack1ll1l11l111_opy_: uuid4().__str__(),
                TestFramework.bstack1ll111l1ll1_opy_: TestFramework.bstack1ll1111l1l1_opy_,
                TestFramework.bstack1l1llll1l11_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll1111ll11_opy_: [],
                TestFramework.bstack1ll111l111l_opy_: hook_name,
                TestFramework.bstack1ll1l1ll111_opy_: bstack1l1lllll111_opy_.bstack1ll11ll1l1l_opy_()
            }
            bstack1ll11111111_opy_[key].append(hook)
            bstack1ll111ll1ll_opy_[PytestBDDFramework.bstack1ll1l111ll1_opy_] = key
        elif test_hook_state == bstack1lll1l1ll11_opy_.POST:
            bstack1ll11lllll1_opy_ = bstack1ll11111111_opy_.get(key, [])
            hook = bstack1ll11lllll1_opy_.pop() if bstack1ll11lllll1_opy_ else None
            if hook:
                result = self.__1ll1111l111_opy_(*args)
                if result:
                    bstack1ll1l11llll_opy_ = result.get(bstack11111_opy_ (u"ࠨ࡯ࡶࡶࡦࡳࡲ࡫ࠢሠ"), TestFramework.bstack1ll1111l1l1_opy_)
                    if bstack1ll1l11llll_opy_ != TestFramework.bstack1ll1111l1l1_opy_:
                        hook[TestFramework.bstack1ll111l1ll1_opy_] = bstack1ll1l11llll_opy_
                hook[TestFramework.bstack1ll11l1ll1l_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll1l1ll111_opy_] = bstack1l1lllll111_opy_.bstack1ll11ll1l1l_opy_()
                self.bstack1ll11ll1ll1_opy_(hook)
                logs = hook.get(TestFramework.bstack1l1llllll11_opy_, [])
                self.bstack1ll1l1ll11l_opy_(instance, logs)
                bstack1ll11ll1lll_opy_[key].append(hook)
                bstack1ll111ll1ll_opy_[PytestBDDFramework.bstack1ll11l111ll_opy_] = key
        TestFramework.bstack1ll11l1llll_opy_(instance, bstack1ll111ll1ll_opy_)
        self.logger.debug(bstack11111_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡨࡰࡱ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࡃࡻ࡬ࡧࡼࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢ࡫ࡳࡴࡱࡳࡠࡵࡷࡥࡷࡺࡥࡥ࠿ࡾ࡬ࡴࡵ࡫ࡴࡡࡶࡸࡦࡸࡴࡦࡦࢀࠤ࡭ࡵ࡯࡬ࡵࡢࡪ࡮ࡴࡩࡴࡪࡨࡨࡂࠨሡ") + str(bstack1ll11ll1lll_opy_) + bstack11111_opy_ (u"ࠣࠤሢ"))
    def __1ll111l1l1l_opy_(
        self,
        context: bstack1ll11111l1l_opy_,
        test_framework_state: bstack1lll1ll111l_opy_,
        test_hook_state: bstack1lll1l1ll11_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll111l1lll_opy_(args[0], [bstack11111_opy_ (u"ࠤࡶࡧࡴࡶࡥࠣሣ"), bstack11111_opy_ (u"ࠥࡥࡷ࡭࡮ࡢ࡯ࡨࠦሤ"), bstack11111_opy_ (u"ࠦࡵࡧࡲࡢ࡯ࡶࠦሥ"), bstack11111_opy_ (u"ࠧ࡯ࡤࡴࠤሦ"), bstack11111_opy_ (u"ࠨࡵ࡯࡫ࡷࡸࡪࡹࡴࠣሧ"), bstack11111_opy_ (u"ࠢࡣࡣࡶࡩ࡮ࡪࠢረ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scenario = args[2] if len(args) == 3 else None
        scope = request.scope if hasattr(request, bstack11111_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢሩ")) else fixturedef.get(bstack11111_opy_ (u"ࠤࡶࡧࡴࡶࡥࠣሪ"), None)
        fixturename = request.fixturename if hasattr(request, bstack11111_opy_ (u"ࠥࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࠣራ")) else None
        node = request.node if hasattr(request, bstack11111_opy_ (u"ࠦࡳࡵࡤࡦࠤሬ")) else None
        target = request.node.nodeid if hasattr(node, bstack11111_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧር")) else None
        baseid = fixturedef.get(bstack11111_opy_ (u"ࠨࡢࡢࡵࡨ࡭ࡩࠨሮ"), None) or bstack11111_opy_ (u"ࠢࠣሯ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack11111_opy_ (u"ࠣࡡࡳࡽ࡫ࡻ࡮ࡤ࡫ࡷࡩࡲࠨሰ")):
            target = PytestBDDFramework.__1ll111l1l11_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack11111_opy_ (u"ࠤ࡯ࡳࡨࡧࡴࡪࡱࡱࠦሱ")) else None
            if target and not TestFramework.bstack1ll1ll1111l_opy_(target):
                self.__1ll1l11ll11_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack11111_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡩ࡭ࡽࡺࡵࡳࡧࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡪࡦࡲ࡬ࡣࡣࡦ࡯ࠥࡺࡡࡳࡩࡨࡸࡂࢁࡴࡢࡴࡪࡩࡹࢃࠠࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࡂࢁࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࢁࠥࡴ࡯ࡥࡧࡀࡿࡳࡵࡤࡦࡿࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࠧሲ") + str(test_hook_state) + bstack11111_opy_ (u"ࠦࠧሳ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack11111_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫ࡤࡦࡨࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡩ࡫ࡦࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡷࡥࡷ࡭ࡥࡵ࠿ࠥሴ") + str(target) + bstack11111_opy_ (u"ࠨࠢስ"))
            return None
        instance = TestFramework.bstack1ll1ll1111l_opy_(target)
        if not instance:
            self.logger.warning(bstack11111_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡦࡪࡺࡷࡹࡷ࡫࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰ࡫ࡥࡳࡪ࡬ࡦࡦࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࡃࡻࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡢࡢࡵࡨ࡭ࡩࡃࡻࡣࡣࡶࡩ࡮ࡪࡽࠡࡶࡤࡶ࡬࡫ࡴ࠾ࠤሶ") + str(target) + bstack11111_opy_ (u"ࠣࠤሷ"))
            return None
        bstack1ll1l1lll11_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1l1llll1ll1_opy_, {})
        if os.getenv(bstack11111_opy_ (u"ࠤࡖࡈࡐࡥࡃࡍࡋࡢࡊࡑࡇࡇࡠࡈࡌ࡜࡙࡛ࡒࡆࡕࠥሸ"), bstack11111_opy_ (u"ࠥ࠵ࠧሹ")) == bstack11111_opy_ (u"ࠦ࠶ࠨሺ"):
            bstack1ll1ll11111_opy_ = bstack11111_opy_ (u"ࠧࡀࠢሻ").join((scope, fixturename))
            bstack1ll1111l11l_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll11l11l11_opy_ = {
                bstack11111_opy_ (u"ࠨ࡫ࡦࡻࠥሼ"): bstack1ll1ll11111_opy_,
                bstack11111_opy_ (u"ࠢࡵࡣࡪࡷࠧሽ"): PytestBDDFramework.__1ll1l1l1111_opy_(request.node, scenario),
                bstack11111_opy_ (u"ࠣࡨ࡬ࡼࡹࡻࡲࡦࠤሾ"): fixturedef,
                bstack11111_opy_ (u"ࠤࡶࡧࡴࡶࡥࠣሿ"): scope,
                bstack11111_opy_ (u"ࠥࡸࡾࡶࡥࠣቀ"): None,
            }
            try:
                if test_hook_state == bstack1lll1l1ll11_opy_.POST and callable(getattr(args[-1], bstack11111_opy_ (u"ࠦ࡬࡫ࡴࡠࡴࡨࡷࡺࡲࡴࠣቁ"), None)):
                    bstack1ll11l11l11_opy_[bstack11111_opy_ (u"ࠧࡺࡹࡱࡧࠥቂ")] = TestFramework.bstack1ll1111llll_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll1l1ll11_opy_.PRE:
                bstack1ll11l11l11_opy_[bstack11111_opy_ (u"ࠨࡵࡶ࡫ࡧࠦቃ")] = uuid4().__str__()
                bstack1ll11l11l11_opy_[PytestBDDFramework.bstack1l1llll1l11_opy_] = bstack1ll1111l11l_opy_
            elif test_hook_state == bstack1lll1l1ll11_opy_.POST:
                bstack1ll11l11l11_opy_[PytestBDDFramework.bstack1ll11l1ll1l_opy_] = bstack1ll1111l11l_opy_
            if bstack1ll1ll11111_opy_ in bstack1ll1l1lll11_opy_:
                bstack1ll1l1lll11_opy_[bstack1ll1ll11111_opy_].update(bstack1ll11l11l11_opy_)
                self.logger.debug(bstack11111_opy_ (u"ࠢࡶࡲࡧࡥࡹ࡫ࡤࠡࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࡃࡻࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫࠽ࠣቄ") + str(bstack1ll1l1lll11_opy_[bstack1ll1ll11111_opy_]) + bstack11111_opy_ (u"ࠣࠤቅ"))
            else:
                bstack1ll1l1lll11_opy_[bstack1ll1ll11111_opy_] = bstack1ll11l11l11_opy_
                self.logger.debug(bstack11111_opy_ (u"ࠤࡶࡥࡻ࡫ࡤࠡࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࡃࡻࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࢂࠦࡳࡤࡱࡳࡩࡂࢁࡳࡤࡱࡳࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫࠽ࡼࡶࡨࡷࡹࡥࡦࡪࡺࡷࡹࡷ࡫ࡽࠡࡶࡵࡥࡨࡱࡥࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࡶࡁࠧቆ") + str(len(bstack1ll1l1lll11_opy_)) + bstack11111_opy_ (u"ࠥࠦቇ"))
        TestFramework.bstack11111111ll_opy_(instance, PytestBDDFramework.bstack1l1llll1ll1_opy_, bstack1ll1l1lll11_opy_)
        self.logger.debug(bstack11111_opy_ (u"ࠦࡸࡧࡶࡦࡦࠣࡪ࡮ࡾࡴࡶࡴࡨࡷࡂࢁ࡬ࡦࡰࠫࡸࡷࡧࡣ࡬ࡧࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࡸ࠯ࡽࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࠦቈ") + str(instance.ref()) + bstack11111_opy_ (u"ࠧࠨ቉"))
        return instance
    def __1ll1l11ll11_opy_(
        self,
        context: bstack1ll11111l1l_opy_,
        test_framework_state: bstack1lll1ll111l_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1ll1ll11_opy_.create_context(target)
        ob = bstack1lll1l11l11_opy_(ctx, self.bstack1ll111llll1_opy_, self.bstack1ll11lll11l_opy_, test_framework_state)
        TestFramework.bstack1ll11l1llll_opy_(ob, {
            TestFramework.bstack1llll111l1l_opy_: context.test_framework_name,
            TestFramework.bstack1lll1l111l1_opy_: context.test_framework_version,
            TestFramework.bstack1ll11l1l1ll_opy_: [],
            PytestBDDFramework.bstack1l1llll1ll1_opy_: {},
            PytestBDDFramework.bstack1ll1l1l1lll_opy_: {},
            PytestBDDFramework.bstack1ll1l11l1ll_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack11111111ll_opy_(ob, TestFramework.bstack1ll1l1l1l1l_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack11111111ll_opy_(ob, TestFramework.bstack1lllll1111l_opy_, context.platform_index)
        TestFramework.bstack1lll1l11111_opy_[ctx.id] = ob
        self.logger.debug(bstack11111_opy_ (u"ࠨࡳࡢࡸࡨࡨࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࠠࡤࡶࡻ࠲࡮ࡪ࠽ࡼࡥࡷࡼ࠳࡯ࡤࡾࠢࡷࡥࡷ࡭ࡥࡵ࠿ࡾࡸࡦࡸࡧࡦࡶࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷࡂࠨቊ") + str(TestFramework.bstack1lll1l11111_opy_.keys()) + bstack11111_opy_ (u"ࠢࠣቋ"))
        return ob
    @staticmethod
    def __1ll1l111111_opy_(instance, args):
        request, feature, scenario = args
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11111_opy_ (u"ࠨ࡫ࡧࠫቌ"): id(step),
                bstack11111_opy_ (u"ࠩࡷࡩࡽࡺࠧቍ"): step.name,
                bstack11111_opy_ (u"ࠪ࡯ࡪࡿࡷࡰࡴࡧࠫ቎"): step.keyword,
            })
        meta = {
            bstack11111_opy_ (u"ࠫ࡫࡫ࡡࡵࡷࡵࡩࠬ቏"): {
                bstack11111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪቐ"): feature.name,
                bstack11111_opy_ (u"࠭ࡰࡢࡶ࡫ࠫቑ"): feature.filename,
                bstack11111_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬቒ"): feature.description
            },
            bstack11111_opy_ (u"ࠨࡵࡦࡩࡳࡧࡲࡪࡱࠪቓ"): {
                bstack11111_opy_ (u"ࠩࡱࡥࡲ࡫ࠧቔ"): scenario.name
            },
            bstack11111_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩቕ"): steps,
            bstack11111_opy_ (u"ࠫࡪࡾࡡ࡮ࡲ࡯ࡩࡸ࠭ቖ"): PytestBDDFramework.__1l1lllllll1_opy_(request.node)
        }
        instance.data.update(
            {
                TestFramework.bstack1l1llll1l1l_opy_: meta
            }
        )
    def bstack1ll11ll1ll1_opy_(self, hook: Dict[str, Any]) -> None:
        bstack11111_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡓࡶࡴࡩࡥࡴࡵࡨࡷࠥࡺࡨࡦࠢࡋࡳࡴࡱࡌࡦࡸࡨࡰࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡷ࡮ࡳࡩ࡭ࡣࡵࠤࡹࡵࠠࡵࡪࡨࠤࡏࡧࡶࡢࠢ࡬ࡱࡵࡲࡥ࡮ࡧࡱࡸࡦࡺࡩࡰࡰ࠱ࠎࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡨࡪࡵࠣࡱࡪࡺࡨࡰࡦ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡆ࡬ࡪࡩ࡫ࡴࠢࡷ࡬ࡪࠦࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭ࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥ࡯࡮ࡴ࡫ࡧࡩࠥࢄ࠯࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠯ࡖࡲ࡯ࡳࡦࡪࡥࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡌ࡯ࡳࠢࡨࡥࡨ࡮ࠠࡧ࡫࡯ࡩࠥ࡯࡮ࠡࡪࡲࡳࡰࡥ࡬ࡦࡸࡨࡰࡤ࡬ࡩ࡭ࡧࡶ࠰ࠥࡸࡥࡱ࡮ࡤࡧࡪࡹࠠࠣࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠦࠥࡽࡩࡵࡪࠣࠦࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠢࠡ࡫ࡱࠤ࡮ࡺࡳࠡࡲࡤࡸ࡭࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡏࡦࠡࡣࠣࡪ࡮ࡲࡥࠡ࡫ࡱࠤࡹ࡮ࡥࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡲࡧࡴࡤࡪࡨࡷࠥࡧࠠ࡮ࡱࡧ࡭࡫࡯ࡥࡥࠢ࡫ࡳࡴࡱ࠭࡭ࡧࡹࡩࡱࠦࡦࡪ࡮ࡨ࠰ࠥ࡯ࡴࠡࡥࡵࡩࡦࡺࡥࡴࠢࡤࠤࡑࡵࡧࡆࡰࡷࡶࡾࠦ࡯ࡣ࡬ࡨࡧࡹࠦࡷࡪࡶ࡫ࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࠡࡦࡨࡸࡦ࡯࡬ࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡕ࡬ࡱ࡮ࡲࡡࡳ࡮ࡼ࠰ࠥ࡯ࡴࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦ࡬ࡰࡥࡤࡸࡪࡪࠠࡪࡰࠣࡌࡴࡵ࡫ࡍࡧࡹࡩࡱ࠵ࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠥࡨࡹࠡࡴࡨࡴࡱࡧࡣࡪࡰࡪࠤࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤࠣࡻ࡮ࡺࡨࠡࠤࡋࡳࡴࡱࡌࡦࡸࡨࡰ࠴ࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠦ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤ࡙࡮ࡥࠡࡥࡵࡩࡦࡺࡥࡥࠢࡏࡳ࡬ࡋ࡮ࡵࡴࡼࠤࡴࡨࡪࡦࡥࡷࡷࠥࡧࡲࡦࠢࡤࡨࡩ࡫ࡤࠡࡶࡲࠤࡹ࡮ࡥࠡࡪࡲࡳࡰ࠭ࡳࠡࠤ࡯ࡳ࡬ࡹࠢࠡ࡮࡬ࡷࡹ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡃࡵ࡫ࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡮࡯ࡰ࡭࠽ࠤ࡙࡮ࡥࠡࡧࡹࡩࡳࡺࠠࡥ࡫ࡦࡸ࡮ࡵ࡮ࡢࡴࡼࠤࡨࡵ࡮ࡵࡣ࡬ࡲ࡮ࡴࡧࠡࡧࡻ࡭ࡸࡺࡩ࡯ࡩࠣࡰࡴ࡭ࡳࠡࡣࡱࡨࠥ࡮࡯ࡰ࡭ࠣ࡭ࡳ࡬࡯ࡳ࡯ࡤࡸ࡮ࡵ࡮࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡩࡱࡲ࡯ࡤࡲࡥࡷࡧ࡯ࡣ࡫࡯࡬ࡦࡵ࠽ࠤࡑ࡯ࡳࡵࠢࡲࡪࠥࡖࡡࡵࡪࠣࡳࡧࡰࡥࡤࡶࡶࠤ࡫ࡸ࡯࡮ࠢࡷ࡬ࡪࠦࡔࡦࡵࡷࡐࡪࡼࡥ࡭ࠢࡰࡳࡳ࡯ࡴࡰࡴ࡬ࡲ࡬࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡨࡵࡪ࡮ࡧࡣࡱ࡫ࡶࡦ࡮ࡢࡪ࡮ࡲࡥࡴ࠼ࠣࡐ࡮ࡹࡴࠡࡱࡩࠤࡕࡧࡴࡩࠢࡲࡦ࡯࡫ࡣࡵࡵࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩࠥࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠢࡰࡳࡳ࡯ࡴࡰࡴ࡬ࡲ࡬࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦ቗")
        global _1ll1111lll1_opy_
        platform_index = os.environ[bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ቘ")]
        bstack1ll111ll111_opy_ = os.path.join(bstack1ll11l1l1l1_opy_, (bstack1ll1l1ll1ll_opy_ + str(platform_index)), bstack1ll1111111l_opy_)
        if not os.path.exists(bstack1ll111ll111_opy_) or not os.path.isdir(bstack1ll111ll111_opy_):
            return
        logs = hook.get(bstack11111_opy_ (u"ࠢ࡭ࡱࡪࡷࠧ቙"), [])
        with os.scandir(bstack1ll111ll111_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll1111lll1_opy_:
                    self.logger.info(bstack11111_opy_ (u"ࠣࡒࡤࡸ࡭ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡱࡴࡲࡧࡪࡹࡳࡦࡦࠣࡿࢂࠨቚ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack11111_opy_ (u"ࠤࠥቛ")
                    log_entry = bstack1ll1l11ll1l_opy_(
                        kind=bstack11111_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧቜ"),
                        message=bstack11111_opy_ (u"ࠦࠧቝ"),
                        level=bstack11111_opy_ (u"ࠧࠨ቞"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1ll1l1111ll_opy_=entry.stat().st_size,
                        bstack1ll11ll11ll_opy_=bstack11111_opy_ (u"ࠨࡍࡂࡐࡘࡅࡑࡥࡕࡑࡎࡒࡅࡉࠨ቟"),
                        bstack1l1l1ll_opy_=os.path.abspath(entry.path),
                        bstack1l1llllll1l_opy_=hook.get(TestFramework.bstack1ll1l11l111_opy_)
                    )
                    logs.append(log_entry)
                    _1ll1111lll1_opy_.add(abs_path)
        platform_index = os.environ[bstack11111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧበ")]
        bstack1l1llll1lll_opy_ = os.path.join(bstack1ll11l1l1l1_opy_, (bstack1ll1l1ll1ll_opy_ + str(platform_index)), bstack1ll1111111l_opy_, bstack1ll11l11ll1_opy_)
        if not os.path.exists(bstack1l1llll1lll_opy_) or not os.path.isdir(bstack1l1llll1lll_opy_):
            self.logger.info(bstack11111_opy_ (u"ࠣࡐࡲࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤ࡫ࡵࡵ࡯ࡦࠣࡥࡹࡀࠠࡼࡿࠥቡ").format(bstack1l1llll1lll_opy_))
        else:
            self.logger.info(bstack11111_opy_ (u"ࠤࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡪࡷࡵ࡭ࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼ࠾ࠥࢁࡽࠣቢ").format(bstack1l1llll1lll_opy_))
            with os.scandir(bstack1l1llll1lll_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll1111lll1_opy_:
                        self.logger.info(bstack11111_opy_ (u"ࠥࡔࡦࡺࡨࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡳࡶࡴࡩࡥࡴࡵࡨࡨࠥࢁࡽࠣባ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack11111_opy_ (u"ࠦࠧቤ")
                        log_entry = bstack1ll1l11ll1l_opy_(
                            kind=bstack11111_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢብ"),
                            message=bstack11111_opy_ (u"ࠨࠢቦ"),
                            level=bstack11111_opy_ (u"ࠢࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠦቧ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1ll1l1111ll_opy_=entry.stat().st_size,
                            bstack1ll11ll11ll_opy_=bstack11111_opy_ (u"ࠣࡏࡄࡒ࡚ࡇࡌࡠࡗࡓࡐࡔࡇࡄࠣቨ"),
                            bstack1l1l1ll_opy_=os.path.abspath(entry.path),
                            bstack1ll11l11lll_opy_=hook.get(TestFramework.bstack1ll1l11l111_opy_)
                        )
                        logs.append(log_entry)
                        _1ll1111lll1_opy_.add(abs_path)
        hook[bstack11111_opy_ (u"ࠤ࡯ࡳ࡬ࡹࠢቩ")] = logs
    def bstack1ll1l1ll11l_opy_(
        self,
        bstack1ll111lll11_opy_: bstack1lll1l11l11_opy_,
        entries: List[bstack1ll1l11ll1l_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack11111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡗࡊ࡙ࡓࡊࡑࡑࡣࡎࡊࠢቪ"))
        req.platform_index = TestFramework.get_state(bstack1ll111lll11_opy_, TestFramework.bstack1lllll1111l_opy_)
        req.execution_context.hash = str(bstack1ll111lll11_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll111lll11_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll111lll11_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll111lll11_opy_, TestFramework.bstack1llll111l1l_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll111lll11_opy_, TestFramework.bstack1lll1l111l1_opy_)
            log_entry.uuid = entry.bstack1l1llllll1l_opy_ if entry.bstack1l1llllll1l_opy_ else TestFramework.get_state(bstack1ll111lll11_opy_, TestFramework.bstack1lll11lllll_opy_)
            log_entry.test_framework_state = bstack1ll111lll11_opy_.state.name
            log_entry.message = entry.message.encode(bstack11111_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥቫ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack11111_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢቬ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll1l1111ll_opy_
                log_entry.file_path = entry.bstack1l1l1ll_opy_
        def bstack1ll111111ll_opy_():
            bstack1lll11l111_opy_ = datetime.now()
            try:
                self.bstack1llll1lll11_opy_.LogCreatedEvent(req)
                bstack1ll111lll11_opy_.bstack1l1l111l1_opy_(bstack11111_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡ࡯ࡳ࡬ࡥࡣࡳࡧࡤࡸࡪࡪ࡟ࡦࡸࡨࡲࡹࡥࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠥቭ"), datetime.now() - bstack1lll11l111_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11111_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࡸ࡫࡮ࡥࡡ࡯ࡳ࡬ࡥࡣࡳࡧࡤࡸࡪࡪ࡟ࡦࡸࡨࡲࡹࡥࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠣࡿࢂࠨቮ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11lll1l_opy_.enqueue(bstack1ll111111ll_opy_)
    def __1ll1l11l11l_opy_(self, instance) -> None:
        bstack11111_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡒ࡯ࡢࡦࡶࠤࡨࡻࡳࡵࡱࡰࠤࡹࡧࡧࡴࠢࡩࡳࡷࠦࡴࡩࡧࠣ࡫࡮ࡼࡥ࡯ࠢࡷࡩࡸࡺࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡄࡴࡨࡥࡹ࡫ࡳࠡࡣࠣࡨ࡮ࡩࡴࠡࡥࡲࡲࡹࡧࡩ࡯࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡰࡪࡼࡥ࡭ࠢࡦࡹࡸࡺ࡯࡮ࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࡪࠠࡧࡴࡲࡱࠏࠦࠠࠡࠢࠣࠤࠥࠦࡃࡶࡵࡷࡳࡲ࡚ࡡࡨࡏࡤࡲࡦ࡭ࡥࡳࠢࡤࡲࡩࠦࡵࡱࡦࡤࡸࡪࡹࠠࡵࡪࡨࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࠦࡳࡵࡣࡷࡩࠥࡻࡳࡪࡰࡪࠤࡸ࡫ࡴࡠࡵࡷࡥࡹ࡫࡟ࡦࡰࡷࡶ࡮࡫ࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨቯ")
        bstack1ll111ll1ll_opy_ = {bstack11111_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡡࡰࡩࡹࡧࡤࡢࡶࡤࠦተ"): bstack1l1lllll111_opy_.bstack1ll11ll1l1l_opy_()}
        TestFramework.bstack1ll11l1llll_opy_(instance, bstack1ll111ll1ll_opy_)
    @staticmethod
    def __1ll111l1111_opy_(instance, args):
        request, bstack1ll1l1ll1l1_opy_ = args
        bstack1ll11llllll_opy_ = id(bstack1ll1l1ll1l1_opy_)
        bstack1ll1l111l1l_opy_ = instance.data[TestFramework.bstack1l1llll1l1l_opy_]
        step = next(filter(lambda st: st[bstack11111_opy_ (u"ࠪ࡭ࡩ࠭ቱ")] == bstack1ll11llllll_opy_, bstack1ll1l111l1l_opy_[bstack11111_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪቲ")]), None)
        step.update({
            bstack11111_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩታ"): datetime.now(tz=timezone.utc)
        })
        index = next((i for i, st in enumerate(bstack1ll1l111l1l_opy_[bstack11111_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬቴ")]) if st[bstack11111_opy_ (u"ࠧࡪࡦࠪት")] == step[bstack11111_opy_ (u"ࠨ࡫ࡧࠫቶ")]), None)
        if index is not None:
            bstack1ll1l111l1l_opy_[bstack11111_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨቷ")][index] = step
        instance.data[TestFramework.bstack1l1llll1l1l_opy_] = bstack1ll1l111l1l_opy_
    @staticmethod
    def __1ll1l1lllll_opy_(instance, args):
        bstack11111_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡸࡪࡨࡲࠥࡲࡥ࡯ࠢࡤࡶ࡬ࡹࠠࡪࡵࠣ࠶࠱ࠦࡩࡵࠢࡶ࡭࡬ࡴࡩࡧ࡫ࡨࡷࠥࡺࡨࡦࡴࡨࠤ࡮ࡹࠠ࡯ࡱࠣࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡦࡸࡧࡴࠢࡤࡶࡪࠦ࠭ࠡ࡝ࡵࡩࡶࡻࡥࡴࡶ࠯ࠤࡸࡺࡥࡱ࡟ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡮࡬ࠠࡢࡴࡪࡷࠥࡧࡲࡦࠢ࠶ࠤࡹ࡮ࡥ࡯ࠢࡷ࡬ࡪࠦ࡬ࡢࡵࡷࠤࡻࡧ࡬ࡶࡧࠣ࡭ࡸࠦࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨቸ")
        bstack1ll1l1l111l_opy_ = datetime.now(tz=timezone.utc)
        request = args[0]
        bstack1ll1l1ll1l1_opy_ = args[1]
        bstack1ll11llllll_opy_ = id(bstack1ll1l1ll1l1_opy_)
        bstack1ll1l111l1l_opy_ = instance.data[TestFramework.bstack1l1llll1l1l_opy_]
        step = None
        if bstack1ll11llllll_opy_ is not None and bstack1ll1l111l1l_opy_.get(bstack11111_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪቹ")):
            step = next(filter(lambda st: st[bstack11111_opy_ (u"ࠬ࡯ࡤࠨቺ")] == bstack1ll11llllll_opy_, bstack1ll1l111l1l_opy_[bstack11111_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬቻ")]), None)
            step.update({
                bstack11111_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬቼ"): bstack1ll1l1l111l_opy_,
            })
        if len(args) > 2:
            exception = args[2]
            step.update({
                bstack11111_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨች"): bstack11111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩቾ"),
                bstack11111_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫቿ"): str(exception)
            })
        else:
            if step is not None:
                step.update({
                    bstack11111_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫኀ"): bstack11111_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬኁ"),
                })
        index = next((i for i, st in enumerate(bstack1ll1l111l1l_opy_[bstack11111_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬኂ")]) if st[bstack11111_opy_ (u"ࠧࡪࡦࠪኃ")] == step[bstack11111_opy_ (u"ࠨ࡫ࡧࠫኄ")]), None)
        if index is not None:
            bstack1ll1l111l1l_opy_[bstack11111_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨኅ")][index] = step
        instance.data[TestFramework.bstack1l1llll1l1l_opy_] = bstack1ll1l111l1l_opy_
    @staticmethod
    def __1l1lllllll1_opy_(node):
        try:
            examples = []
            if hasattr(node, bstack11111_opy_ (u"ࠪࡧࡦࡲ࡬ࡴࡲࡨࡧࠬኆ")):
                examples = list(node.callspec.params[bstack11111_opy_ (u"ࠫࡤࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡨࡼࡦࡳࡰ࡭ࡧࠪኇ")].values())
            return examples
        except:
            return []
    def bstack1ll1l1lll1l_opy_(self, instance: bstack1lll1l11l11_opy_, bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_]):
        bstack1ll11l1l11l_opy_ = (
            PytestBDDFramework.bstack1ll1l111ll1_opy_
            if bstack1lllllll1ll_opy_[1] == bstack1lll1l1ll11_opy_.PRE
            else PytestBDDFramework.bstack1ll11l111ll_opy_
        )
        hook = PytestBDDFramework.bstack1ll11lll1ll_opy_(instance, bstack1ll11l1l11l_opy_)
        entries = hook.get(TestFramework.bstack1ll1111ll11_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll11l1l1ll_opy_, []))
        return entries
    def bstack1ll111l11l1_opy_(self, instance: bstack1lll1l11l11_opy_, bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_]):
        bstack1ll11l1l11l_opy_ = (
            PytestBDDFramework.bstack1ll1l111ll1_opy_
            if bstack1lllllll1ll_opy_[1] == bstack1lll1l1ll11_opy_.PRE
            else PytestBDDFramework.bstack1ll11l111ll_opy_
        )
        PytestBDDFramework.bstack1ll1ll111l1_opy_(instance, bstack1ll11l1l11l_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll11l1l1ll_opy_, []).clear()
    @staticmethod
    def bstack1ll11lll1ll_opy_(instance: bstack1lll1l11l11_opy_, bstack1ll11l1l11l_opy_: str):
        bstack1l1llllllll_opy_ = (
            PytestBDDFramework.bstack1ll1l1l1lll_opy_
            if bstack1ll11l1l11l_opy_ == PytestBDDFramework.bstack1ll11l111ll_opy_
            else PytestBDDFramework.bstack1ll1l11l1ll_opy_
        )
        bstack1ll1l111l11_opy_ = TestFramework.get_state(instance, bstack1ll11l1l11l_opy_, None)
        bstack1ll11ll1l11_opy_ = TestFramework.get_state(instance, bstack1l1llllllll_opy_, None) if bstack1ll1l111l11_opy_ else None
        return (
            bstack1ll11ll1l11_opy_[bstack1ll1l111l11_opy_][-1]
            if isinstance(bstack1ll11ll1l11_opy_, dict) and len(bstack1ll11ll1l11_opy_.get(bstack1ll1l111l11_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll1ll111l1_opy_(instance: bstack1lll1l11l11_opy_, bstack1ll11l1l11l_opy_: str):
        hook = PytestBDDFramework.bstack1ll11lll1ll_opy_(instance, bstack1ll11l1l11l_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll1111ll11_opy_, []).clear()
    @staticmethod
    def __1ll1l111lll_opy_(instance: bstack1lll1l11l11_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack11111_opy_ (u"ࠧ࡭ࡥࡵࡡࡵࡩࡨࡵࡲࡥࡵࠥኈ"), None)):
            return
        if os.getenv(bstack11111_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡇࡎࡄࡋࡤࡒࡏࡈࡕࠥ኉"), bstack11111_opy_ (u"ࠢ࠲ࠤኊ")) != bstack11111_opy_ (u"ࠣ࠳ࠥኋ"):
            PytestBDDFramework.logger.warning(bstack11111_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡪࡰࡪࠤࡨࡧࡰ࡭ࡱࡪࠦኌ"))
            return
        bstack1ll11ll11l1_opy_ = {
            bstack11111_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤኍ"): (PytestBDDFramework.bstack1ll1l111ll1_opy_, PytestBDDFramework.bstack1ll1l11l1ll_opy_),
            bstack11111_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨ኎"): (PytestBDDFramework.bstack1ll11l111ll_opy_, PytestBDDFramework.bstack1ll1l1l1lll_opy_),
        }
        for when in (bstack11111_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦ኏"), bstack11111_opy_ (u"ࠨࡣࡢ࡮࡯ࠦነ"), bstack11111_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤኑ")):
            bstack1ll1111l1ll_opy_ = args[1].get_records(when)
            if not bstack1ll1111l1ll_opy_:
                continue
            records = [
                bstack1ll1l11ll1l_opy_(
                    kind=TestFramework.bstack1ll11l1ll11_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack11111_opy_ (u"ࠣ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨࠦኒ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack11111_opy_ (u"ࠤࡦࡶࡪࡧࡴࡦࡦࠥና")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll1111l1ll_opy_
                if isinstance(getattr(r, bstack11111_opy_ (u"ࠥࡱࡪࡹࡳࡢࡩࡨࠦኔ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll11l111l1_opy_, bstack1l1llllllll_opy_ = bstack1ll11ll11l1_opy_.get(when, (None, None))
            bstack1ll11l1lll1_opy_ = TestFramework.get_state(instance, bstack1ll11l111l1_opy_, None) if bstack1ll11l111l1_opy_ else None
            bstack1ll11ll1l11_opy_ = TestFramework.get_state(instance, bstack1l1llllllll_opy_, None) if bstack1ll11l1lll1_opy_ else None
            if isinstance(bstack1ll11ll1l11_opy_, dict) and len(bstack1ll11ll1l11_opy_.get(bstack1ll11l1lll1_opy_, [])) > 0:
                hook = bstack1ll11ll1l11_opy_[bstack1ll11l1lll1_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll1111ll11_opy_ in hook:
                    hook[TestFramework.bstack1ll1111ll11_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll11l1l1ll_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1l1lllll1l1_opy_(args) -> Dict[str, Any]:
        request, feature, scenario = args
        test_id = request.node.nodeid
        test_name = PytestBDDFramework.__1ll11l11l1l_opy_(request.node, scenario)
        bstack1ll11llll1l_opy_ = feature.filename
        if not test_id or not test_name or not bstack1ll11llll1l_opy_:
            return None
        code = None
        return {
            TestFramework.bstack1lll11lllll_opy_: uuid4().__str__(),
            TestFramework.bstack1ll11l1111l_opy_: test_id,
            TestFramework.bstack1ll111ll1l1_opy_: test_name,
            TestFramework.bstack1ll1l1llll1_opy_: test_id,
            TestFramework.bstack1ll11llll11_opy_: bstack1ll11llll1l_opy_,
            TestFramework.bstack1ll11111ll1_opy_: PytestBDDFramework.__1ll1l1l1111_opy_(feature, scenario),
            TestFramework.bstack1ll1l1l11ll_opy_: code,
            TestFramework.bstack1llll11l1l1_opy_: TestFramework.bstack1ll11ll1111_opy_,
            TestFramework.bstack1lll11ll11l_opy_: test_name
        }
    @staticmethod
    def __1ll11l11l1l_opy_(node, scenario):
        if hasattr(node, bstack11111_opy_ (u"ࠫࡨࡧ࡬࡭ࡵࡳࡩࡨ࠭ን")):
            parts = node.nodeid.rsplit(bstack11111_opy_ (u"ࠧࡡࠢኖ"))
            params = parts[-1]
            return bstack11111_opy_ (u"ࠨࡻࡾࠢ࡞ࡿࢂࠨኗ").format(scenario.name, params)
        return scenario.name
    @staticmethod
    def __1ll1l1l1111_opy_(feature, scenario) -> List[str]:
        return (list(feature.tags) if hasattr(feature, bstack11111_opy_ (u"ࠧࡵࡣࡪࡷࠬኘ")) else []) + (list(scenario.tags) if hasattr(scenario, bstack11111_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭ኙ")) else [])
    @staticmethod
    def __1ll111l1l11_opy_(location):
        return bstack11111_opy_ (u"ࠤ࠽࠾ࠧኚ").join(filter(lambda x: isinstance(x, str), location))