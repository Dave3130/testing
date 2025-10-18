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
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1ll1llllll1_opy_ import bstack1ll1ll1lll1_opy_
from browserstack_sdk.sdk_cli.utils.bstack111l1lll11_opy_ import bstack1l1llll1lll_opy_
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1lll1ll11ll_opy_,
    bstack1lll1llll11_opy_,
    bstack1lll1lll11l_opy_,
    bstack1l1llllll1l_opy_,
    bstack1ll11ll1ll1_opy_,
)
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from datetime import datetime, timezone
from typing import List, Dict, Any
import traceback
from bstack_utils.helper import bstack1ll1l1lllll_opy_
from bstack_utils.bstack11l1l1111l_opy_ import bstack1llll1ll11l_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.bstack1lll11lll1l_opy_ import bstack1lll11llll1_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll11l1l111_opy_ import bstack1ll1111ll1l_opy_
from bstack_utils.bstack11llllll_opy_ import bstack1l11lll1_opy_
bstack1ll1l111ll1_opy_ = bstack1ll1l1lllll_opy_()
bstack1ll1l1ll11l_opy_ = 1.0
bstack1ll1l11ll11_opy_ = bstack1l1lll1_opy_ (u"࡙ࠥࡵࡲ࡯ࡢࡦࡨࡨࡆࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴ࠯ࠥᕥ")
bstack11llll1l1l1_opy_ = bstack1l1lll1_opy_ (u"࡙ࠦ࡫ࡳࡵࡎࡨࡺࡪࡲࠢᕦ")
bstack11llll1l1ll_opy_ = bstack1l1lll1_opy_ (u"ࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤᕧ")
bstack11llll1ll11_opy_ = bstack1l1lll1_opy_ (u"ࠨࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭ࠤᕨ")
bstack11llll1l11l_opy_ = bstack1l1lll1_opy_ (u"ࠢࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࡌࡴࡵ࡫ࡆࡸࡨࡲࡹࠨᕩ")
_1ll11l11ll1_opy_ = set()
class bstack1l11lll1111_opy_(TestFramework):
    bstack1ll11llllll_opy_ = bstack1l1lll1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪࡺࡷࡹࡷ࡫ࡳࠣᕪ")
    bstack1ll11lll1ll_opy_ = bstack1l1lll1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸࡥࡳࡵࡣࡵࡸࡪࡪࠢᕫ")
    bstack1ll11ll1111_opy_ = bstack1l1lll1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡹ࡟ࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࠤᕬ")
    bstack1ll111l1lll_opy_ = bstack1l1lll1_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟࡭ࡣࡶࡸࡤࡹࡴࡢࡴࡷࡩࡩࠨᕭ")
    bstack1ll1111l1ll_opy_ = bstack1l1lll1_opy_ (u"ࠧࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠ࡮ࡤࡷࡹࡥࡦࡪࡰ࡬ࡷ࡭࡫ࡤࠣᕮ")
    bstack1ll1l1ll111_opy_: bool
    bstack1lll11lll1l_opy_: bstack1lll11llll1_opy_  = None
    bstack1lllll1ll11_opy_ = None
    bstack1ll1l1l1lll_opy_ = [
        bstack1lll1ll11ll_opy_.BEFORE_ALL,
        bstack1lll1ll11ll_opy_.AFTER_ALL,
        bstack1lll1ll11ll_opy_.BEFORE_EACH,
        bstack1lll1ll11ll_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll1ll11111_opy_: Dict[str, str],
        bstack1ll1111l1l1_opy_: List[str]=[bstack1l1lll1_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࠨᕯ")],
        bstack1lll11lll1l_opy_: bstack1lll11llll1_opy_=None,
        bstack1lllll1ll11_opy_=None
    ):
        super().__init__(bstack1ll1111l1l1_opy_, bstack1ll1ll11111_opy_, bstack1lll11lll1l_opy_)
        self.bstack1ll1l1ll111_opy_ = any(bstack1l1lll1_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺࠢᕰ") in item.lower() for item in bstack1ll1111l1l1_opy_)
        self.bstack1lllll1ll11_opy_ = bstack1lllll1ll11_opy_
    def track_event(
        self,
        context: bstack1l1llllll1l_opy_,
        test_framework_state: bstack1lll1ll11ll_opy_,
        test_hook_state: bstack1lll1lll11l_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1lll1ll11ll_opy_.TEST or test_framework_state in bstack1l11lll1111_opy_.bstack1ll1l1l1lll_opy_:
            bstack1l1llll1lll_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1lll1ll11ll_opy_.NONE:
            self.logger.warning(bstack1l1lll1_opy_ (u"ࠣ࡫ࡪࡲࡴࡸࡥࡥࠢࡦࡥࡱࡲࡢࡢࡥ࡮ࠤࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂࠦࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥ࠾ࠤᕱ") + str(test_hook_state) + bstack1l1lll1_opy_ (u"ࠤࠥᕲ"))
            return
        if not self.bstack1ll1l1ll111_opy_:
            self.logger.warning(bstack1l1lll1_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲࡸࡻࡰࡱࡱࡵࡸࡪࡪࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡀࠦᕳ") + str(str(self.bstack1ll1111l1l1_opy_)) + bstack1l1lll1_opy_ (u"ࠦࠧᕴ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack1l1lll1_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡥࡹࡲࡨࡧࡹ࡫ࡤࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᕵ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠨࠢᕶ"))
            return
        instance = self.__1ll1l1lll11_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡢࡴࡪࡷࡂࠨᕷ") + str(args) + bstack1l1lll1_opy_ (u"ࠣࠤᕸ"))
            return
        try:
            if instance!= None and test_framework_state in bstack1l11lll1111_opy_.bstack1ll1l1l1lll_opy_ and test_hook_state == bstack1lll1lll11l_opy_.PRE:
                bstack1ll1l11l111_opy_ = bstack1llll1ll11l_opy_.bstack1ll1ll1111l_opy_(EVENTS.bstack111ll1l1l_opy_.value)
                name = str(EVENTS.bstack111ll1l1l_opy_.name)+bstack1l1lll1_opy_ (u"ࠤ࠽ࠦᕹ")+str(test_framework_state.name)
                TestFramework.bstack1ll11ll1l11_opy_(instance, name, bstack1ll1l11l111_opy_)
        except Exception as e:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢ࡫ࡳࡴࡱࠠࡦࡴࡵࡳࡷࠦࡰࡳࡧ࠽ࠤࢀࢃࠢᕺ").format(e))
        try:
            if not TestFramework.bstack1llllll111l_opy_(instance, TestFramework.bstack1ll1l1l1l1l_opy_) and test_hook_state == bstack1lll1lll11l_opy_.PRE:
                test = bstack1l11lll1111_opy_.__1ll1l111lll_opy_(args[0])
                if test:
                    instance.data.update(test)
                    self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡱࡵࡡࡥࡧࡧࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡵࡩ࡫࠮ࠩࡾࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࠦᕻ") + str(test_hook_state) + bstack1l1lll1_opy_ (u"ࠧࠨᕼ"))
            if test_framework_state == bstack1lll1ll11ll_opy_.TEST:
                if test_hook_state == bstack1lll1lll11l_opy_.PRE and not TestFramework.bstack1llllll111l_opy_(instance, TestFramework.bstack1ll11111111_opy_):
                    TestFramework.bstack1llll1lllll_opy_(instance, TestFramework.bstack1ll11111111_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1l1lll1_opy_ (u"ࠨࡳࡦࡶࠣࡸࡪࡹࡴ࠮ࡵࡷࡥࡷࡺࠠࡧࡱࡵࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡵࡩ࡫࠮ࠩࡾࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࠦᕽ") + str(test_hook_state) + bstack1l1lll1_opy_ (u"ࠢࠣᕾ"))
                elif test_hook_state == bstack1lll1lll11l_opy_.POST and not TestFramework.bstack1llllll111l_opy_(instance, TestFramework.bstack1ll111111ll_opy_):
                    TestFramework.bstack1llll1lllll_opy_(instance, TestFramework.bstack1ll111111ll_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡵࡨࡸࠥࡺࡥࡴࡶ࠰ࡩࡳࡪࠠࡧࡱࡵࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡵࡩ࡫࠮ࠩࡾࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࠦᕿ") + str(test_hook_state) + bstack1l1lll1_opy_ (u"ࠤࠥᖀ"))
            elif test_framework_state == bstack1lll1ll11ll_opy_.LOG and test_hook_state == bstack1lll1lll11l_opy_.POST:
                bstack1l11lll1111_opy_.__1l1lllll1l1_opy_(instance, *args)
            elif test_framework_state == bstack1lll1ll11ll_opy_.LOG_REPORT and test_hook_state == bstack1lll1lll11l_opy_.POST:
                self.__1ll1l11111l_opy_(instance, *args)
                self.__1ll1l111111_opy_(instance)
            elif test_framework_state in bstack1l11lll1111_opy_.bstack1ll1l1l1lll_opy_:
                self.__1l1lllll111_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢ࡫ࡥࡳࡪ࡬ࡦࡦࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࠦᖁ") + str(instance.ref()) + bstack1l1lll1_opy_ (u"ࠦࠧᖂ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll111l1l1l_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in bstack1l11lll1111_opy_.bstack1ll1l1l1lll_opy_ and test_hook_state == bstack1lll1lll11l_opy_.POST:
                name = str(EVENTS.bstack111ll1l1l_opy_.name)+bstack1l1lll1_opy_ (u"ࠧࡀࠢᖃ")+str(test_framework_state.name)
                bstack1ll1l11l111_opy_ = TestFramework.bstack1ll1l11llll_opy_(instance, name)
                bstack1llll1ll11l_opy_.end(EVENTS.bstack111ll1l1l_opy_.value, bstack1ll1l11l111_opy_+bstack1l1lll1_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᖄ"), bstack1ll1l11l111_opy_+bstack1l1lll1_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᖅ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡩࡱࡲ࡯ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠣᖆ").format(e))
    def bstack1ll11llll11_opy_(self):
        return self.bstack1ll1l1ll111_opy_
    def __1ll11l11l11_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack1l1lll1_opy_ (u"ࠤࡪࡩࡹࡥࡲࡦࡵࡸࡰࡹࠨᖇ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll1l1l1l11_opy_(rep, [bstack1l1lll1_opy_ (u"ࠥࡻ࡭࡫࡮ࠣᖈ"), bstack1l1lll1_opy_ (u"ࠦࡴࡻࡴࡤࡱࡰࡩࠧᖉ"), bstack1l1lll1_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧᖊ"), bstack1l1lll1_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨᖋ"), bstack1l1lll1_opy_ (u"ࠢࡴ࡭࡬ࡴࡵ࡫ࡤࠣᖌ"), bstack1l1lll1_opy_ (u"ࠣ࡮ࡲࡲ࡬ࡸࡥࡱࡴࡷࡩࡽࡺࠢᖍ")])
        return None
    def __1ll1l11111l_opy_(self, instance: bstack1lll1llll11_opy_, *args):
        result = self.__1ll11l11l11_opy_(*args)
        if not result:
            return
        failure = None
        bstack11111l1111_opy_ = None
        if result.get(bstack1l1lll1_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥᖎ"), None) == bstack1l1lll1_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥᖏ") and len(args) > 1 and getattr(args[1], bstack1l1lll1_opy_ (u"ࠦࡪࡾࡣࡪࡰࡩࡳࠧᖐ"), None) is not None:
            failure = [{bstack1l1lll1_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᖑ"): [args[1].excinfo.exconly(), result.get(bstack1l1lll1_opy_ (u"ࠨ࡬ࡰࡰࡪࡶࡪࡶࡲࡵࡧࡻࡸࠧᖒ"), None)]}]
            bstack11111l1111_opy_ = bstack1l1lll1_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣᖓ") if bstack1l1lll1_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࠦᖔ") in getattr(args[1].excinfo, bstack1l1lll1_opy_ (u"ࠤࡷࡽࡵ࡫࡮ࡢ࡯ࡨࠦᖕ"), bstack1l1lll1_opy_ (u"ࠥࠦᖖ")) else bstack1l1lll1_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧᖗ")
        bstack1ll111l111l_opy_ = result.get(bstack1l1lll1_opy_ (u"ࠧࡵࡵࡵࡥࡲࡱࡪࠨᖘ"), TestFramework.bstack1ll11l1l11l_opy_)
        if bstack1ll111l111l_opy_ != TestFramework.bstack1ll11l1l11l_opy_:
            TestFramework.bstack1llll1lllll_opy_(instance, TestFramework.bstack1ll11l1l1l1_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll1l111l11_opy_(instance, {
            TestFramework.bstack1lll1ll111l_opy_: failure,
            TestFramework.bstack1ll1111llll_opy_: bstack11111l1111_opy_,
            TestFramework.bstack1lll1l11111_opy_: bstack1ll111l111l_opy_,
        })
    def __1ll1l1lll11_opy_(
        self,
        context: bstack1l1llllll1l_opy_,
        test_framework_state: bstack1lll1ll11ll_opy_,
        test_hook_state: bstack1lll1lll11l_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1lll1ll11ll_opy_.SETUP_FIXTURE:
            instance = self.__1ll11111lll_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll11l11111_opy_ bstack1l1lllll11l_opy_ this to be bstack1l1lll1_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨᖙ")
            if test_framework_state == bstack1lll1ll11ll_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll1l11l1l1_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1lll1ll11ll_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack1l1lll1_opy_ (u"ࠢ࡯ࡱࡧࡩࠧᖚ"), None), bstack1l1lll1_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣᖛ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack1l1lll1_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤᖜ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll111lllll_opy_(target) if target else None
        return instance
    def __1l1lllll111_opy_(
        self,
        instance: bstack1lll1llll11_opy_,
        test_framework_state: bstack1lll1ll11ll_opy_,
        test_hook_state: bstack1lll1lll11l_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll1l1ll1ll_opy_ = TestFramework.get_state(instance, bstack1l11lll1111_opy_.bstack1ll11lll1ll_opy_, {})
        if not key in bstack1ll1l1ll1ll_opy_:
            bstack1ll1l1ll1ll_opy_[key] = []
        bstack1l1llllll11_opy_ = TestFramework.get_state(instance, bstack1l11lll1111_opy_.bstack1ll11ll1111_opy_, {})
        if not key in bstack1l1llllll11_opy_:
            bstack1l1llllll11_opy_[key] = []
        bstack1ll1l11l1ll_opy_ = {
            bstack1l11lll1111_opy_.bstack1ll11lll1ll_opy_: bstack1ll1l1ll1ll_opy_,
            bstack1l11lll1111_opy_.bstack1ll11ll1111_opy_: bstack1l1llllll11_opy_,
        }
        if test_hook_state == bstack1lll1lll11l_opy_.PRE:
            hook = {
                bstack1l1lll1_opy_ (u"ࠥ࡯ࡪࡿࠢᖝ"): key,
                TestFramework.bstack1ll11l111ll_opy_: uuid4().__str__(),
                TestFramework.bstack1l1lllllll1_opy_: TestFramework.bstack1ll11lllll1_opy_,
                TestFramework.bstack1ll11lll11l_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll1111111l_opy_: [],
                TestFramework.bstack1ll11111l11_opy_: args[1] if len(args) > 1 else bstack1l1lll1_opy_ (u"ࠫࠬᖞ"),
                TestFramework.bstack1ll1l11l11l_opy_: bstack1ll1111ll1l_opy_.bstack1ll1l1l1ll1_opy_()
            }
            bstack1ll1l1ll1ll_opy_[key].append(hook)
            bstack1ll1l11l1ll_opy_[bstack1l11lll1111_opy_.bstack1ll111l1lll_opy_] = key
        elif test_hook_state == bstack1lll1lll11l_opy_.POST:
            bstack1ll111l11l1_opy_ = bstack1ll1l1ll1ll_opy_.get(key, [])
            hook = bstack1ll111l11l1_opy_.pop() if bstack1ll111l11l1_opy_ else None
            if hook:
                result = self.__1ll11l11l11_opy_(*args)
                if result:
                    bstack1ll1l1111l1_opy_ = result.get(bstack1l1lll1_opy_ (u"ࠧࡵࡵࡵࡥࡲࡱࡪࠨᖟ"), TestFramework.bstack1ll11lllll1_opy_)
                    if bstack1ll1l1111l1_opy_ != TestFramework.bstack1ll11lllll1_opy_:
                        hook[TestFramework.bstack1l1lllllll1_opy_] = bstack1ll1l1111l1_opy_
                hook[TestFramework.bstack1ll11l1ll11_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll1l11l11l_opy_]= bstack1ll1111ll1l_opy_.bstack1ll1l1l1ll1_opy_()
                self.bstack1ll11llll1l_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll11lll111_opy_, [])
                if logs: self.bstack1ll111l1l11_opy_(instance, logs)
                bstack1l1llllll11_opy_[key].append(hook)
                bstack1ll1l11l1ll_opy_[bstack1l11lll1111_opy_.bstack1ll1111l1ll_opy_] = key
        TestFramework.bstack1ll1l111l11_opy_(instance, bstack1ll1l11l1ll_opy_)
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡮࡯ࡰ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࡂࢁ࡫ࡦࡻࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡪࡲࡳࡰࡹ࡟ࡴࡶࡤࡶࡹ࡫ࡤ࠾ࡽ࡫ࡳࡴࡱࡳࡠࡵࡷࡥࡷࡺࡥࡥࡿࠣ࡬ࡴࡵ࡫ࡴࡡࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡁࠧᖠ") + str(bstack1l1llllll11_opy_) + bstack1l1lll1_opy_ (u"ࠢࠣᖡ"))
    def __1ll11111lll_opy_(
        self,
        context: bstack1l1llllll1l_opy_,
        test_framework_state: bstack1lll1ll11ll_opy_,
        test_hook_state: bstack1lll1lll11l_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll1l1l1l11_opy_(args[0], [bstack1l1lll1_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢᖢ"), bstack1l1lll1_opy_ (u"ࠤࡤࡶ࡬ࡴࡡ࡮ࡧࠥᖣ"), bstack1l1lll1_opy_ (u"ࠥࡴࡦࡸࡡ࡮ࡵࠥᖤ"), bstack1l1lll1_opy_ (u"ࠦ࡮ࡪࡳࠣᖥ"), bstack1l1lll1_opy_ (u"ࠧࡻ࡮ࡪࡶࡷࡩࡸࡺࠢᖦ"), bstack1l1lll1_opy_ (u"ࠨࡢࡢࡵࡨ࡭ࡩࠨᖧ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scope = request.scope if hasattr(request, bstack1l1lll1_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨᖨ")) else fixturedef.get(bstack1l1lll1_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢᖩ"), None)
        fixturename = request.fixturename if hasattr(request, bstack1l1lll1_opy_ (u"ࠤࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࠢᖪ")) else None
        node = request.node if hasattr(request, bstack1l1lll1_opy_ (u"ࠥࡲࡴࡪࡥࠣᖫ")) else None
        target = request.node.nodeid if hasattr(node, bstack1l1lll1_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦᖬ")) else None
        baseid = fixturedef.get(bstack1l1lll1_opy_ (u"ࠧࡨࡡࡴࡧ࡬ࡨࠧᖭ"), None) or bstack1l1lll1_opy_ (u"ࠨࠢᖮ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack1l1lll1_opy_ (u"ࠢࡠࡲࡼࡪࡺࡴࡣࡪࡶࡨࡱࠧᖯ")):
            target = bstack1l11lll1111_opy_.__1l1llll1ll1_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack1l1lll1_opy_ (u"ࠣ࡮ࡲࡧࡦࡺࡩࡰࡰࠥᖰ")) else None
            if target and not TestFramework.bstack1ll111lllll_opy_(target):
                self.__1ll1l11l1l1_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡨ࡬ࡼࡹࡻࡲࡦࡡࡨࡺࡪࡴࡴ࠻ࠢࡩࡥࡱࡲࡢࡢࡥ࡮ࠤࡹࡧࡲࡨࡧࡷࡁࢀࡺࡡࡳࡩࡨࡸࢂࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡳࡵࡤࡦ࠿ࡾࡲࡴࡪࡥࡾࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࠦᖱ") + str(test_hook_state) + bstack1l1lll1_opy_ (u"ࠥࠦᖲ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack1l1lll1_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡪ࡮ࡾࡴࡶࡴࡨࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡪࡥࡧ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡨࡪ࡬ࡽࠡࡵࡦࡳࡵ࡫࠽ࡼࡵࡦࡳࡵ࡫ࡽࠡࡶࡤࡶ࡬࡫ࡴ࠾ࠤᖳ") + str(target) + bstack1l1lll1_opy_ (u"ࠧࠨᖴ"))
            return None
        instance = TestFramework.bstack1ll111lllll_opy_(target)
        if not instance:
            self.logger.warning(bstack1l1lll1_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥࡥࡷࡧࡱࡸ࠿ࠦࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࡂࢁࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥࡨࡡࡴࡧ࡬ࡨࡂࢁࡢࡢࡵࡨ࡭ࡩࢃࠠࡵࡣࡵ࡫ࡪࡺ࠽ࠣᖵ") + str(target) + bstack1l1lll1_opy_ (u"ࠢࠣᖶ"))
            return None
        bstack1ll11l1ll1l_opy_ = TestFramework.get_state(instance, bstack1l11lll1111_opy_.bstack1ll11llllll_opy_, {})
        if os.getenv(bstack1l1lll1_opy_ (u"ࠣࡕࡇࡏࡤࡉࡌࡊࡡࡉࡐࡆࡍ࡟ࡇࡋ࡛ࡘ࡚ࡘࡅࡔࠤᖷ"), bstack1l1lll1_opy_ (u"ࠤ࠴ࠦᖸ")) == bstack1l1lll1_opy_ (u"ࠥ࠵ࠧᖹ"):
            bstack1ll111lll11_opy_ = bstack1l1lll1_opy_ (u"ࠦ࠿ࠨᖺ").join((scope, fixturename))
            bstack1ll1l1l11ll_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll1111l111_opy_ = {
                bstack1l1lll1_opy_ (u"ࠧࡱࡥࡺࠤᖻ"): bstack1ll111lll11_opy_,
                bstack1l1lll1_opy_ (u"ࠨࡴࡢࡩࡶࠦᖼ"): bstack1l11lll1111_opy_.__1ll1l111l1l_opy_(request.node),
                bstack1l1lll1_opy_ (u"ࠢࡧ࡫ࡻࡸࡺࡸࡥࠣᖽ"): fixturedef,
                bstack1l1lll1_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢᖾ"): scope,
                bstack1l1lll1_opy_ (u"ࠤࡷࡽࡵ࡫ࠢᖿ"): None,
            }
            try:
                if test_hook_state == bstack1lll1lll11l_opy_.POST and callable(getattr(args[-1], bstack1l1lll1_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡳࡧࡶࡹࡱࡺࠢᗀ"), None)):
                    bstack1ll1111l111_opy_[bstack1l1lll1_opy_ (u"ࠦࡹࡿࡰࡦࠤᗁ")] = TestFramework.bstack1ll11l11lll_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll1lll11l_opy_.PRE:
                bstack1ll1111l111_opy_[bstack1l1lll1_opy_ (u"ࠧࡻࡵࡪࡦࠥᗂ")] = uuid4().__str__()
                bstack1ll1111l111_opy_[bstack1l11lll1111_opy_.bstack1ll11lll11l_opy_] = bstack1ll1l1l11ll_opy_
            elif test_hook_state == bstack1lll1lll11l_opy_.POST:
                bstack1ll1111l111_opy_[bstack1l11lll1111_opy_.bstack1ll11l1ll11_opy_] = bstack1ll1l1l11ll_opy_
            if bstack1ll111lll11_opy_ in bstack1ll11l1ll1l_opy_:
                bstack1ll11l1ll1l_opy_[bstack1ll111lll11_opy_].update(bstack1ll1111l111_opy_)
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠨࡵࡱࡦࡤࡸࡪࡪࠠࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࡂࢁࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡃࠢᗃ") + str(bstack1ll11l1ll1l_opy_[bstack1ll111lll11_opy_]) + bstack1l1lll1_opy_ (u"ࠢࠣᗄ"))
            else:
                bstack1ll11l1ll1l_opy_[bstack1ll111lll11_opy_] = bstack1ll1111l111_opy_
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡵࡤࡺࡪࡪࠠࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࡂࢁࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡃࡻࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࢃࠠࡵࡴࡤࡧࡰ࡫ࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࡀࠦᗅ") + str(len(bstack1ll11l1ll1l_opy_)) + bstack1l1lll1_opy_ (u"ࠤࠥᗆ"))
        TestFramework.bstack1llll1lllll_opy_(instance, bstack1l11lll1111_opy_.bstack1ll11llllll_opy_, bstack1ll11l1ll1l_opy_)
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠥࡷࡦࡼࡥࡥࠢࡩ࡭ࡽࡺࡵࡳࡧࡶࡁࢀࡲࡥ࡯ࠪࡷࡶࡦࡩ࡫ࡦࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࡷ࠮ࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࠥᗇ") + str(instance.ref()) + bstack1l1lll1_opy_ (u"ࠦࠧᗈ"))
        return instance
    def __1ll1l11l1l1_opy_(
        self,
        context: bstack1l1llllll1l_opy_,
        test_framework_state: bstack1lll1ll11ll_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1ll1lll1_opy_.create_context(target)
        ob = bstack1lll1llll11_opy_(ctx, self.bstack1ll1111l1l1_opy_, self.bstack1ll1ll11111_opy_, test_framework_state)
        TestFramework.bstack1ll1l111l11_opy_(ob, {
            TestFramework.bstack1llll1l111l_opy_: context.test_framework_name,
            TestFramework.bstack1lll1l1l111_opy_: context.test_framework_version,
            TestFramework.bstack1ll1l1l111l_opy_: [],
            bstack1l11lll1111_opy_.bstack1ll11llllll_opy_: {},
            bstack1l11lll1111_opy_.bstack1ll11ll1111_opy_: {},
            bstack1l11lll1111_opy_.bstack1ll11lll1ll_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1llll1lllll_opy_(ob, TestFramework.bstack1ll11l1l1ll_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1llll1lllll_opy_(ob, TestFramework.bstack1llll1l1ll1_opy_, context.platform_index)
        TestFramework.bstack1lll1l1l1l1_opy_[ctx.id] = ob
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠧࡹࡡࡷࡧࡧࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࠦࡣࡵࡺ࠱࡭ࡩࡃࡻࡤࡶࡻ࠲࡮ࡪࡽࠡࡶࡤࡶ࡬࡫ࡴ࠾ࡽࡷࡥࡷ࡭ࡥࡵࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶࡁࠧᗉ") + str(TestFramework.bstack1lll1l1l1l1_opy_.keys()) + bstack1l1lll1_opy_ (u"ࠨࠢᗊ"))
        return ob
    def bstack1ll11lll1l1_opy_(self, instance: bstack1lll1llll11_opy_, bstack1lllll1llll_opy_: Tuple[bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_]):
        bstack1ll111l1ll1_opy_ = (
            bstack1l11lll1111_opy_.bstack1ll111l1lll_opy_
            if bstack1lllll1llll_opy_[1] == bstack1lll1lll11l_opy_.PRE
            else bstack1l11lll1111_opy_.bstack1ll1111l1ll_opy_
        )
        hook = bstack1l11lll1111_opy_.bstack1ll1l1l11l1_opy_(instance, bstack1ll111l1ll1_opy_)
        entries = hook.get(TestFramework.bstack1ll1111111l_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll1l1l111l_opy_, []))
        return entries
    def bstack1ll11ll111l_opy_(self, instance: bstack1lll1llll11_opy_, bstack1lllll1llll_opy_: Tuple[bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_]):
        bstack1ll111l1ll1_opy_ = (
            bstack1l11lll1111_opy_.bstack1ll111l1lll_opy_
            if bstack1lllll1llll_opy_[1] == bstack1lll1lll11l_opy_.PRE
            else bstack1l11lll1111_opy_.bstack1ll1111l1ll_opy_
        )
        bstack1l11lll1111_opy_.bstack1ll11l1111l_opy_(instance, bstack1ll111l1ll1_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll1l1l111l_opy_, []).clear()
    def bstack1ll11llll1l_opy_(self, hook: Dict[str, Any]) -> None:
        bstack1l1lll1_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡕࡸ࡯ࡤࡧࡶࡷࡪࡹࠠࡵࡪࡨࠤࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥࡹࡩ࡮࡫࡯ࡥࡷࠦࡴࡰࠢࡷ࡬ࡪࠦࡊࡢࡸࡤࠤ࡮ࡳࡰ࡭ࡧࡰࡩࡳࡺࡡࡵ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡕࡪ࡬ࡷࠥࡳࡥࡵࡪࡲࡨ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡈ࡮ࡥࡤ࡭ࡶࠤࡹ࡮ࡥࠡࡊࡲࡳࡰࡒࡥࡷࡧ࡯ࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠࡪࡰࡶ࡭ࡩ࡫ࠠࡿ࠱࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠱ࡘࡴࡱࡵࡡࡥࡧࡧࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡇࡱࡵࠤࡪࡧࡣࡩࠢࡩ࡭ࡱ࡫ࠠࡪࡰࠣ࡬ࡴࡵ࡫ࡠ࡮ࡨࡺࡪࡲ࡟ࡧ࡫࡯ࡩࡸ࠲ࠠࡳࡧࡳࡰࡦࡩࡥࡴࠢࠥࡘࡪࡹࡴࡍࡧࡹࡩࡱࠨࠠࡸ࡫ࡷ࡬ࠥࠨࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭ࠤࠣ࡭ࡳࠦࡩࡵࡵࠣࡴࡦࡺࡨ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡊࡨࠣࡥࠥ࡬ࡩ࡭ࡧࠣ࡭ࡳࠦࡴࡩࡧࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦ࡭ࡢࡶࡦ࡬ࡪࡹࠠࡢࠢࡰࡳࡩ࡯ࡦࡪࡧࡧࠤ࡭ࡵ࡯࡬࠯࡯ࡩࡻ࡫࡬ࠡࡨ࡬ࡰࡪ࠲ࠠࡪࡶࠣࡧࡷ࡫ࡡࡵࡧࡶࠤࡦࠦࡌࡰࡩࡈࡲࡹࡸࡹࠡࡱࡥ࡮ࡪࡩࡴࠡࡹ࡬ࡸ࡭ࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠣࡨࡪࡺࡡࡪ࡮ࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡗ࡮ࡳࡩ࡭ࡣࡵࡰࡾ࠲ࠠࡪࡶࠣࡴࡷࡵࡣࡦࡵࡶࡩࡸࠦࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡ࡮ࡲࡧࡦࡺࡥࡥࠢ࡬ࡲࠥࡎ࡯ࡰ࡭ࡏࡩࡻ࡫࡬࠰ࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࡍࡵ࡯࡬ࡇࡹࡩࡳࡺࠠࡣࡻࠣࡶࡪࡶ࡬ࡢࡥ࡬ࡲ࡬ࠦࠢࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠦࠥࡽࡩࡵࡪࠣࠦࡍࡵ࡯࡬ࡎࡨࡺࡪࡲ࠯ࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࡌࡴࡵ࡫ࡆࡸࡨࡲࡹࠨ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡔࡩࡧࠣࡧࡷ࡫ࡡࡵࡧࡧࠤࡑࡵࡧࡆࡰࡷࡶࡾࠦ࡯ࡣ࡬ࡨࡧࡹࡹࠠࡢࡴࡨࠤࡦࡪࡤࡦࡦࠣࡸࡴࠦࡴࡩࡧࠣ࡬ࡴࡵ࡫ࠨࡵࠣࠦࡱࡵࡧࡴࠤࠣࡰ࡮ࡹࡴ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡅࡷ࡭ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡩࡱࡲ࡯࠿ࠦࡔࡩࡧࠣࡩࡻ࡫࡮ࡵࠢࡧ࡭ࡨࡺࡩࡰࡰࡤࡶࡾࠦࡣࡰࡰࡷࡥ࡮ࡴࡩ࡯ࡩࠣࡩࡽ࡯ࡳࡵ࡫ࡱ࡫ࠥࡲ࡯ࡨࡵࠣࡥࡳࡪࠠࡩࡱࡲ࡯ࠥ࡯࡮ࡧࡱࡵࡱࡦࡺࡩࡰࡰ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡫ࡳࡴࡱ࡟࡭ࡧࡹࡩࡱࡥࡦࡪ࡮ࡨࡷ࠿ࠦࡌࡪࡵࡷࠤࡴ࡬ࠠࡑࡣࡷ࡬ࠥࡵࡢ࡫ࡧࡦࡸࡸࠦࡦࡳࡱࡰࠤࡹ࡮ࡥࠡࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠤࡲࡵ࡮ࡪࡶࡲࡶ࡮ࡴࡧ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡣࡷ࡬ࡰࡩࡥ࡬ࡦࡸࡨࡰࡤ࡬ࡩ࡭ࡧࡶ࠾ࠥࡒࡩࡴࡶࠣࡳ࡫ࠦࡐࡢࡶ࡫ࠤࡴࡨࡪࡦࡥࡷࡷࠥ࡬ࡲࡰ࡯ࠣࡸ࡭࡫ࠠࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠤࡲࡵ࡮ࡪࡶࡲࡶ࡮ࡴࡧ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᗋ")
        global _1ll11l11ll1_opy_
        platform_index = os.environ[bstack1l1lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨᗌ")]
        bstack1ll11l111l1_opy_ = os.path.join(bstack1ll1l111ll1_opy_, (bstack1ll1l11ll11_opy_ + str(platform_index)), bstack11llll1ll11_opy_)
        if not os.path.exists(bstack1ll11l111l1_opy_) or not os.path.isdir(bstack1ll11l111l1_opy_):
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠤࡇ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥࡪ࡯ࡦࡵࠣࡲࡴࡺࠠࡦࡺ࡬ࡷࡹࡹࠠࡵࡱࠣࡴࡷࡵࡣࡦࡵࡶࠤࢀࢃࠢᗍ").format(bstack1ll11l111l1_opy_))
            return
        logs = hook.get(bstack1l1lll1_opy_ (u"ࠥࡰࡴ࡭ࡳࠣᗎ"), [])
        with os.scandir(bstack1ll11l111l1_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll11l11ll1_opy_:
                    self.logger.info(bstack1l1lll1_opy_ (u"ࠦࡕࡧࡴࡩࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡴࡷࡵࡣࡦࡵࡶࡩࡩࠦࡻࡾࠤᗏ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack1l1lll1_opy_ (u"ࠧࠨᗐ")
                    log_entry = bstack1ll11ll1ll1_opy_(
                        kind=bstack1l1lll1_opy_ (u"ࠨࡔࡆࡕࡗࡣࡆ࡚ࡔࡂࡅࡋࡑࡊࡔࡔࠣᗑ"),
                        message=bstack1l1lll1_opy_ (u"ࠢࠣᗒ"),
                        level=bstack1l1lll1_opy_ (u"ࠣࠤᗓ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1l1llllllll_opy_=entry.stat().st_size,
                        bstack1ll111l11ll_opy_=bstack1l1lll1_opy_ (u"ࠤࡐࡅࡓ࡛ࡁࡍࡡࡘࡔࡑࡕࡁࡅࠤᗔ"),
                        bstack11l1l_opy_=os.path.abspath(entry.path),
                        bstack1ll1l1llll1_opy_=hook.get(TestFramework.bstack1ll11l111ll_opy_)
                    )
                    logs.append(log_entry)
                    _1ll11l11ll1_opy_.add(abs_path)
        platform_index = os.environ[bstack1l1lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪᗕ")]
        bstack1ll1l11lll1_opy_ = os.path.join(bstack1ll1l111ll1_opy_, (bstack1ll1l11ll11_opy_ + str(platform_index)), bstack11llll1ll11_opy_, bstack11llll1l11l_opy_)
        if not os.path.exists(bstack1ll1l11lll1_opy_) or not os.path.isdir(bstack1ll1l11lll1_opy_):
            self.logger.info(bstack1l1lll1_opy_ (u"ࠦࡓࡵࠠࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࡌࡴࡵ࡫ࡆࡸࡨࡲࡹࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠࡧࡱࡸࡲࡩࠦࡡࡵ࠼ࠣࡿࢂࠨᗖ").format(bstack1ll1l11lll1_opy_))
        else:
            self.logger.info(bstack1l1lll1_opy_ (u"ࠧࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࡎ࡯ࡰ࡭ࡈࡺࡪࡴࡴࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦࡦࡳࡱࡰࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿ࠺ࠡࡽࢀࠦᗗ").format(bstack1ll1l11lll1_opy_))
            with os.scandir(bstack1ll1l11lll1_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll11l11ll1_opy_:
                        self.logger.info(bstack1l1lll1_opy_ (u"ࠨࡐࡢࡶ࡫ࠤࡦࡲࡲࡦࡣࡧࡽࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡤࠡࡽࢀࠦᗘ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack1l1lll1_opy_ (u"ࠢࠣᗙ")
                        log_entry = bstack1ll11ll1ll1_opy_(
                            kind=bstack1l1lll1_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡁࡕࡖࡄࡇࡍࡓࡅࡏࡖࠥᗚ"),
                            message=bstack1l1lll1_opy_ (u"ࠤࠥᗛ"),
                            level=bstack1l1lll1_opy_ (u"ࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠢᗜ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1l1llllllll_opy_=entry.stat().st_size,
                            bstack1ll111l11ll_opy_=bstack1l1lll1_opy_ (u"ࠦࡒࡇࡎࡖࡃࡏࡣ࡚ࡖࡌࡐࡃࡇࠦᗝ"),
                            bstack11l1l_opy_=os.path.abspath(entry.path),
                            bstack1l1llll1l1l_opy_=hook.get(TestFramework.bstack1ll11l111ll_opy_)
                        )
                        logs.append(log_entry)
                        _1ll11l11ll1_opy_.add(abs_path)
        hook[bstack1l1lll1_opy_ (u"ࠧࡲ࡯ࡨࡵࠥᗞ")] = logs
    def bstack1ll111l1l11_opy_(
        self,
        bstack1ll1l1111ll_opy_: bstack1lll1llll11_opy_,
        entries: List[bstack1ll11ll1ll1_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack1l1lll1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡌࡊࡡࡅࡍࡓࡥࡓࡆࡕࡖࡍࡔࡔ࡟ࡊࡆࠥᗟ"))
        req.platform_index = TestFramework.get_state(bstack1ll1l1111ll_opy_, TestFramework.bstack1llll1l1ll1_opy_)
        req.execution_context.hash = str(bstack1ll1l1111ll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll1l1111ll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll1l1111ll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll1l1111ll_opy_, TestFramework.bstack1llll1l111l_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll1l1111ll_opy_, TestFramework.bstack1lll1l1l111_opy_)
            log_entry.uuid = entry.bstack1ll1l1llll1_opy_
            log_entry.test_framework_state = bstack1ll1l1111ll_opy_.state.name
            log_entry.message = entry.message.encode(bstack1l1lll1_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᗠ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            log_entry.level = bstack1l1lll1_opy_ (u"ࠣࠤᗡ")
            if entry.kind == bstack1l1lll1_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡂࡖࡗࡅࡈࡎࡍࡆࡐࡗࠦᗢ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1l1llllllll_opy_
                log_entry.file_path = entry.bstack11l1l_opy_
        def bstack1ll111lll1l_opy_():
            bstack11ll11ll1_opy_ = datetime.now()
            try:
                self.bstack1lllll1ll11_opy_.LogCreatedEvent(req)
                bstack1ll1l1111ll_opy_.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥ࡬ࡰࡩࡢࡧࡷ࡫ࡡࡵࡧࡧࡣࡪࡼࡥ࡯ࡶࡢࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࠢᗣ"), datetime.now() - bstack11ll11ll1_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1l1lll1_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࡵࡨࡲࡩࡥ࡬ࡰࡩࡢࡧࡷ࡫ࡡࡵࡧࡧࡣࡪࡼࡥ࡯ࡶࡢࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࠠࡼࡿࠥᗤ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11lll1l_opy_.enqueue(bstack1ll111lll1l_opy_)
    def __1ll1l111111_opy_(self, instance) -> None:
        bstack1l1lll1_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡏࡳࡦࡪࡳࠡࡥࡸࡷࡹࡵ࡭ࠡࡶࡤ࡫ࡸࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡨ࡫ࡹࡩࡳࠦࡴࡦࡵࡷࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡈࡸࡥࡢࡶࡨࡷࠥࡧࠠࡥ࡫ࡦࡸࠥࡩ࡯࡯ࡶࡤ࡭ࡳ࡯࡮ࡨࠢࡷࡩࡸࡺࠠ࡭ࡧࡹࡩࡱࠦࡣࡶࡵࡷࡳࡲࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡇࡺࡹࡴࡰ࡯ࡗࡥ࡬ࡓࡡ࡯ࡣࡪࡩࡷࠦࡡ࡯ࡦࠣࡹࡵࡪࡡࡵࡧࡶࠤࡹ࡮ࡥࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠣࡷࡹࡧࡴࡦࠢࡸࡷ࡮ࡴࡧࠡࡵࡨࡸࡤࡹࡴࡢࡶࡨࡣࡪࡴࡴࡳ࡫ࡨࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᗥ")
        bstack1ll1l11l1ll_opy_ = {bstack1l1lll1_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲࡥ࡭ࡦࡶࡤࡨࡦࡺࡡࠣᗦ"): bstack1ll1111ll1l_opy_.bstack1ll1l1l1ll1_opy_()}
        from browserstack_sdk.sdk_cli.test_framework import TestFramework
        TestFramework.bstack1ll1l111l11_opy_(instance, bstack1ll1l11l1ll_opy_)
    @staticmethod
    def bstack1ll1l1l11l1_opy_(instance: bstack1lll1llll11_opy_, bstack1ll111l1ll1_opy_: str):
        bstack1ll1111ll11_opy_ = (
            bstack1l11lll1111_opy_.bstack1ll11ll1111_opy_
            if bstack1ll111l1ll1_opy_ == bstack1l11lll1111_opy_.bstack1ll1111l1ll_opy_
            else bstack1l11lll1111_opy_.bstack1ll11lll1ll_opy_
        )
        bstack1ll1l1l1111_opy_ = TestFramework.get_state(instance, bstack1ll111l1ll1_opy_, None)
        bstack1ll11l1lll1_opy_ = TestFramework.get_state(instance, bstack1ll1111ll11_opy_, None) if bstack1ll1l1l1111_opy_ else None
        return (
            bstack1ll11l1lll1_opy_[bstack1ll1l1l1111_opy_][-1]
            if isinstance(bstack1ll11l1lll1_opy_, dict) and len(bstack1ll11l1lll1_opy_.get(bstack1ll1l1l1111_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll11l1111l_opy_(instance: bstack1lll1llll11_opy_, bstack1ll111l1ll1_opy_: str):
        hook = bstack1l11lll1111_opy_.bstack1ll1l1l11l1_opy_(instance, bstack1ll111l1ll1_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll1111111l_opy_, []).clear()
    @staticmethod
    def __1l1lllll1l1_opy_(instance: bstack1lll1llll11_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack1l1lll1_opy_ (u"ࠢࡨࡧࡷࡣࡷ࡫ࡣࡰࡴࡧࡷࠧᗧ"), None)):
            return
        if os.getenv(bstack1l1lll1_opy_ (u"ࠣࡕࡇࡏࡤࡉࡌࡊࡡࡉࡐࡆࡍ࡟ࡍࡑࡊࡗࠧᗨ"), bstack1l1lll1_opy_ (u"ࠤ࠴ࠦᗩ")) != bstack1l1lll1_opy_ (u"ࠥ࠵ࠧᗪ"):
            bstack1l11lll1111_opy_.logger.warning(bstack1l1lll1_opy_ (u"ࠦ࡮࡭࡮ࡰࡴ࡬ࡲ࡬ࠦࡣࡢࡲ࡯ࡳ࡬ࠨᗫ"))
            return
        bstack1ll11ll11ll_opy_ = {
            bstack1l1lll1_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦᗬ"): (bstack1l11lll1111_opy_.bstack1ll111l1lll_opy_, bstack1l11lll1111_opy_.bstack1ll11lll1ll_opy_),
            bstack1l1lll1_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࠣᗭ"): (bstack1l11lll1111_opy_.bstack1ll1111l1ll_opy_, bstack1l11lll1111_opy_.bstack1ll11ll1111_opy_),
        }
        for when in (bstack1l1lll1_opy_ (u"ࠢࡴࡧࡷࡹࡵࠨᗮ"), bstack1l1lll1_opy_ (u"ࠣࡥࡤࡰࡱࠨᗯ"), bstack1l1lll1_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࠦᗰ")):
            bstack1ll111ll111_opy_ = args[1].get_records(when)
            if not bstack1ll111ll111_opy_:
                continue
            records = [
                bstack1ll11ll1ll1_opy_(
                    kind=TestFramework.bstack1ll1l1ll1l1_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack1l1lll1_opy_ (u"ࠥࡰࡪࡼࡥ࡭ࡰࡤࡱࡪࠨᗱ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack1l1lll1_opy_ (u"ࠦࡨࡸࡥࡢࡶࡨࡨࠧᗲ")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll111ll111_opy_
                if isinstance(getattr(r, bstack1l1lll1_opy_ (u"ࠧࡳࡥࡴࡵࡤ࡫ࡪࠨᗳ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll111ll1ll_opy_, bstack1ll1111ll11_opy_ = bstack1ll11ll11ll_opy_.get(when, (None, None))
            bstack1ll1ll111l1_opy_ = TestFramework.get_state(instance, bstack1ll111ll1ll_opy_, None) if bstack1ll111ll1ll_opy_ else None
            bstack1ll11l1lll1_opy_ = TestFramework.get_state(instance, bstack1ll1111ll11_opy_, None) if bstack1ll1ll111l1_opy_ else None
            if isinstance(bstack1ll11l1lll1_opy_, dict) and len(bstack1ll11l1lll1_opy_.get(bstack1ll1ll111l1_opy_, [])) > 0:
                hook = bstack1ll11l1lll1_opy_[bstack1ll1ll111l1_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll1111111l_opy_ in hook:
                    hook[TestFramework.bstack1ll1111111l_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll1l1l111l_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll1l111lll_opy_(test) -> Dict[str, Any]:
        test_id = bstack1l11lll1111_opy_.__1l1llll1ll1_opy_(test.location) if hasattr(test, bstack1l1lll1_opy_ (u"ࠨ࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠣᗴ")) else getattr(test, bstack1l1lll1_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢᗵ"), None)
        test_name = test.name if hasattr(test, bstack1l1lll1_opy_ (u"ࠣࡰࡤࡱࡪࠨᗶ")) else None
        bstack1ll111llll1_opy_ = test.fspath.strpath if hasattr(test, bstack1l1lll1_opy_ (u"ࠤࡩࡷࡵࡧࡴࡩࠤᗷ")) and test.fspath else None
        if not test_id or not test_name or not bstack1ll111llll1_opy_:
            return None
        code = None
        if hasattr(test, bstack1l1lll1_opy_ (u"ࠥࡳࡧࡰࠢᗸ")):
            try:
                import inspect
                code = inspect.getsource(test.obj)
            except:
                pass
        bstack11llll1l111_opy_ = []
        try:
            bstack11llll1l111_opy_ = bstack1l11lll1_opy_.bstack1l1ll11l_opy_(test)
        except:
            bstack1l11lll1111_opy_.logger.warning(bstack1l1lll1_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡺࡥࡴࡶࠣࡷࡨࡵࡰࡦࡵ࠯ࠤࡹ࡫ࡳࡵࠢࡶࡧࡴࡶࡥࡴࠢࡺ࡭ࡱࡲࠠࡣࡧࠣࡶࡪࡹ࡯࡭ࡸࡨࡨࠥ࡯࡮ࠡࡅࡏࡍࠧᗹ"))
        return {
            TestFramework.bstack1llll11lll1_opy_: uuid4().__str__(),
            TestFramework.bstack1ll1l1l1l1l_opy_: test_id,
            TestFramework.bstack1ll11ll11l1_opy_: test_name,
            TestFramework.bstack1ll111ll1l1_opy_: getattr(test, bstack1l1lll1_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧᗺ"), None),
            TestFramework.bstack1ll111l1111_opy_: bstack1ll111llll1_opy_,
            TestFramework.bstack1ll11111l1l_opy_: bstack1l11lll1111_opy_.__1ll1l111l1l_opy_(test),
            TestFramework.bstack1ll11l1llll_opy_: code,
            TestFramework.bstack1lll1l11111_opy_: TestFramework.bstack1ll11l1l11l_opy_,
            TestFramework.bstack1lll111lll1_opy_: test_id,
            TestFramework.bstack1l1111l11ll_opy_: bstack11llll1l111_opy_
        }
    @staticmethod
    def __1ll1l111l1l_opy_(test) -> List[str]:
        markers = []
        current = test
        while current:
            own_markers = getattr(current, bstack1l1lll1_opy_ (u"ࠨ࡯ࡸࡰࡢࡱࡦࡸ࡫ࡦࡴࡶࠦᗻ"), [])
            markers.extend([getattr(m, bstack1l1lll1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᗼ"), None) for m in own_markers if getattr(m, bstack1l1lll1_opy_ (u"ࠣࡰࡤࡱࡪࠨᗽ"), None)])
            current = getattr(current, bstack1l1lll1_opy_ (u"ࠤࡳࡥࡷ࡫࡮ࡵࠤᗾ"), None)
        return markers
    @staticmethod
    def __1l1llll1ll1_opy_(location):
        return bstack1l1lll1_opy_ (u"ࠥ࠾࠿ࠨᗿ").join(filter(lambda x: isinstance(x, str), location))