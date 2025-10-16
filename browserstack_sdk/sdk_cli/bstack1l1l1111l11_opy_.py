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
from datetime import datetime, timezone
import os
import builtins
from pathlib import Path
from typing import Any, Tuple, Callable, List
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import bstack1111111l11_opy_, bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_
from browserstack_sdk.sdk_cli.bstack1111111111_opy_ import bstack1llll1ll11l_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l11l1_opy_ import bstack1lll11l111l_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1ll1_opy_ import bstack1lllll1ll11_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll11l1ll_opy_, bstack1lll1l11l11_opy_, bstack1llll1l11l1_opy_, bstack1ll1l1l1ll1_opy_
from json import dumps, JSONEncoder
import grpc
from browserstack_sdk import sdk_pb2 as structs
import sys
import traceback
import time
import json
from bstack_utils.helper import bstack1lll1l1l11l_opy_, bstack1ll1111l1ll_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
bstack1l11ll11l11_opy_ = [bstack1lllll1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᎰ"), bstack1lllll1_opy_ (u"ࠣࡲࡤࡶࡪࡴࡴࠣᎱ"), bstack1lllll1_opy_ (u"ࠤࡦࡳࡳ࡬ࡩࡨࠤᎲ"), bstack1lllll1_opy_ (u"ࠥࡷࡪࡹࡳࡪࡱࡱࠦᎳ"), bstack1lllll1_opy_ (u"ࠦࡵࡧࡴࡩࠤᎴ")]
bstack1ll11l1111l_opy_ = bstack1ll1111l1ll_opy_()
bstack1ll11ll11ll_opy_ = bstack1lllll1_opy_ (u"࡛ࠧࡰ࡭ࡱࡤࡨࡪࡪࡁࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶ࠱ࠧᎵ")
bstack1l11l11l11l_opy_ = {
    bstack1lllll1_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡰࡺࡶ࡫ࡳࡳ࠴ࡉࡵࡧࡰࠦᎶ"): bstack1l11ll11l11_opy_,
    bstack1lllll1_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡱࡻࡷ࡬ࡴࡴ࠮ࡑࡣࡦ࡯ࡦ࡭ࡥࠣᎷ"): bstack1l11ll11l11_opy_,
    bstack1lllll1_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡲࡼࡸ࡭ࡵ࡮࠯ࡏࡲࡨࡺࡲࡥࠣᎸ"): bstack1l11ll11l11_opy_,
    bstack1lllll1_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡳࡽࡹ࡮࡯࡯࠰ࡆࡰࡦࡹࡳࠣᎹ"): bstack1l11ll11l11_opy_,
    bstack1lllll1_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡴࡾࡺࡨࡰࡰ࠱ࡊࡺࡴࡣࡵ࡫ࡲࡲࠧᎺ"): bstack1l11ll11l11_opy_
    + [
        bstack1lllll1_opy_ (u"ࠦࡴࡸࡩࡨ࡫ࡱࡥࡱࡴࡡ࡮ࡧࠥᎻ"),
        bstack1lllll1_opy_ (u"ࠧࡱࡥࡺࡹࡲࡶࡩࡹࠢᎼ"),
        bstack1lllll1_opy_ (u"ࠨࡦࡪࡺࡷࡹࡷ࡫ࡩ࡯ࡨࡲࠦᎽ"),
        bstack1lllll1_opy_ (u"ࠢ࡬ࡧࡼࡻࡴࡸࡤࡴࠤᎾ"),
        bstack1lllll1_opy_ (u"ࠣࡥࡤࡰࡱࡹࡰࡦࡥࠥᎿ"),
        bstack1lllll1_opy_ (u"ࠤࡦࡥࡱࡲ࡯ࡣ࡬ࠥᏀ"),
        bstack1lllll1_opy_ (u"ࠥࡷࡹࡧࡲࡵࠤᏁ"),
        bstack1lllll1_opy_ (u"ࠦࡸࡺ࡯ࡱࠤᏂ"),
        bstack1lllll1_opy_ (u"ࠧࡪࡵࡳࡣࡷ࡭ࡴࡴࠢᏃ"),
        bstack1lllll1_opy_ (u"ࠨࡷࡩࡧࡱࠦᏄ"),
    ],
    bstack1lllll1_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮࡮ࡣ࡬ࡲ࠳࡙ࡥࡴࡵ࡬ࡳࡳࠨᏅ"): [bstack1lllll1_opy_ (u"ࠣࡵࡷࡥࡷࡺࡰࡢࡶ࡫ࠦᏆ"), bstack1lllll1_opy_ (u"ࠤࡷࡩࡸࡺࡳࡧࡣ࡬ࡰࡪࡪࠢᏇ"), bstack1lllll1_opy_ (u"ࠥࡸࡪࡹࡴࡴࡥࡲࡰࡱ࡫ࡣࡵࡧࡧࠦᏈ"), bstack1lllll1_opy_ (u"ࠦ࡮ࡺࡥ࡮ࡵࠥᏉ")],
    bstack1lllll1_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡩ࡯࡯ࡨ࡬࡫࠳ࡉ࡯࡯ࡨ࡬࡫ࠧᏊ"): [bstack1lllll1_opy_ (u"ࠨࡩ࡯ࡸࡲࡧࡦࡺࡩࡰࡰࡢࡴࡦࡸࡡ࡮ࡵࠥᏋ"), bstack1lllll1_opy_ (u"ࠢࡢࡴࡪࡷࠧᏌ")],
    bstack1lllll1_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡨ࡬ࡼࡹࡻࡲࡦࡵ࠱ࡊ࡮ࡾࡴࡶࡴࡨࡈࡪ࡬ࠢᏍ"): [bstack1lllll1_opy_ (u"ࠤࡶࡧࡴࡶࡥࠣᏎ"), bstack1lllll1_opy_ (u"ࠥࡥࡷ࡭࡮ࡢ࡯ࡨࠦᏏ"), bstack1lllll1_opy_ (u"ࠦ࡫ࡻ࡮ࡤࠤᏐ"), bstack1lllll1_opy_ (u"ࠧࡶࡡࡳࡣࡰࡷࠧᏑ"), bstack1lllll1_opy_ (u"ࠨࡵ࡯࡫ࡷࡸࡪࡹࡴࠣᏒ"), bstack1lllll1_opy_ (u"ࠢࡪࡦࡶࠦᏓ")],
    bstack1lllll1_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡨ࡬ࡼࡹࡻࡲࡦࡵ࠱ࡗࡺࡨࡒࡦࡳࡸࡩࡸࡺࠢᏔ"): [bstack1lllll1_opy_ (u"ࠤࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࠢᏕ"), bstack1lllll1_opy_ (u"ࠥࡴࡦࡸࡡ࡮ࠤᏖ"), bstack1lllll1_opy_ (u"ࠦࡵࡧࡲࡢ࡯ࡢ࡭ࡳࡪࡥࡹࠤᏗ")],
    bstack1lllll1_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡸࡵ࡯ࡰࡨࡶ࠳ࡉࡡ࡭࡮ࡌࡲ࡫ࡵࠢᏘ"): [bstack1lllll1_opy_ (u"ࠨࡷࡩࡧࡱࠦᏙ"), bstack1lllll1_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࠢᏚ")],
    bstack1lllll1_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯࡯ࡤࡶࡰ࠴ࡳࡵࡴࡸࡧࡹࡻࡲࡦࡵ࠱ࡒࡴࡪࡥࡌࡧࡼࡻࡴࡸࡤࡴࠤᏛ"): [bstack1lllll1_opy_ (u"ࠤࡱࡳࡩ࡫ࠢᏜ"), bstack1lllll1_opy_ (u"ࠥࡴࡦࡸࡥ࡯ࡶࠥᏝ")],
    bstack1lllll1_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡲࡧࡲ࡬࠰ࡶࡸࡷࡻࡣࡵࡷࡵࡩࡸ࠴ࡍࡢࡴ࡮ࠦᏞ"): [bstack1lllll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᏟ"), bstack1lllll1_opy_ (u"ࠨࡡࡳࡩࡶࠦᏠ"), bstack1lllll1_opy_ (u"ࠢ࡬ࡹࡤࡶ࡬ࡹࠢᏡ")],
}
_1ll11l11l11_opy_ = set()
class bstack1l1l11llll1_opy_(bstack1llll1ll11l_opy_):
    bstack1l11ll11ll1_opy_ = bstack1lllll1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡤࡦࡨࡨࡶࡷ࡫ࡤࠣᏢ")
    bstack1l11l111l1l_opy_ = bstack1lllll1_opy_ (u"ࠤࡌࡒࡋࡕࠢᏣ")
    bstack1l11ll11lll_opy_ = bstack1lllll1_opy_ (u"ࠥࡉࡗࡘࡏࡓࠤᏤ")
    bstack1l11l1l1111_opy_: Callable
    bstack1l11l1lll11_opy_: Callable
    def __init__(self, bstack1l1l1l111ll_opy_, bstack1ll1lll1ll1_opy_):
        super().__init__()
        self.bstack1l11l11l1l1_opy_ = bstack1ll1lll1ll1_opy_
        if os.getenv(bstack1lllll1_opy_ (u"ࠦࡘࡊࡋࡠࡅࡏࡍࡤࡌࡌࡂࡉࡢࡓ࠶࠷࡙ࠣᏥ"), bstack1lllll1_opy_ (u"ࠧ࠷ࠢᏦ")) != bstack1lllll1_opy_ (u"ࠨ࠱ࠣᏧ") or not self.is_enabled():
            self.logger.warning(bstack1lllll1_opy_ (u"ࠢࠣᏨ") + str(self.__class__.__name__) + bstack1lllll1_opy_ (u"ࠣࠢࡧ࡭ࡸࡧࡢ࡭ࡧࡧࠦᏩ"))
            return
        TestFramework.bstack11111111ll_opy_((bstack1llll11l1ll_opy_.TEST, bstack1llll1l11l1_opy_.PRE), self.bstack1lll1l1lll1_opy_)
        TestFramework.bstack11111111ll_opy_((bstack1llll11l1ll_opy_.TEST, bstack1llll1l11l1_opy_.POST), self.bstack1llll111l1l_opy_)
        for event in bstack1llll11l1ll_opy_:
            for state in bstack1llll1l11l1_opy_:
                TestFramework.bstack11111111ll_opy_((event, state), self.bstack1l11l11111l_opy_)
        bstack1l1l1l111ll_opy_.bstack11111111ll_opy_((bstack1llll1ll1ll_opy_.bstack1lllll1l1l1_opy_, bstack1lllll1lll1_opy_.POST), self.bstack1l11l11l111_opy_)
        self.bstack1l11l1l1111_opy_ = sys.stdout.write
        sys.stdout.write = self.bstack1l11l1l1l1l_opy_(bstack1l1l11llll1_opy_.bstack1l11l111l1l_opy_, self.bstack1l11l1l1111_opy_)
        self.bstack1l11l1lll11_opy_ = sys.stderr.write
        sys.stderr.write = self.bstack1l11l1l1l1l_opy_(bstack1l1l11llll1_opy_.bstack1l11ll11lll_opy_, self.bstack1l11l1lll11_opy_)
        self.bstack1l11ll1l11l_opy_ = builtins.print
        builtins.print = self.bstack1l11l111l11_opy_()
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l11111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        if f.bstack1ll11ll1ll1_opy_() and instance:
            bstack1l11l1l111l_opy_ = datetime.now()
            test_framework_state, test_hook_state = bstack1lllll111ll_opy_
            if test_framework_state == bstack1llll11l1ll_opy_.SETUP_FIXTURE:
                return
            elif test_framework_state == bstack1llll11l1ll_opy_.LOG:
                bstack1l11llll11_opy_ = datetime.now()
                entries = f.bstack1ll1l111111_opy_(instance, bstack1lllll111ll_opy_)
                if entries:
                    self.bstack1ll11111l11_opy_(instance, entries)
                    instance.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡧࡱࡨࡤࡲ࡯ࡨࡡࡦࡶࡪࡧࡴࡦࡦࡢࡩࡻ࡫࡮ࡵࠤᏪ"), datetime.now() - bstack1l11llll11_opy_)
                    f.bstack1ll11lllll1_opy_(instance, bstack1lllll111ll_opy_)
                instance.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠥࡳ࠶࠷ࡹ࠻ࡱࡱࡣࡦࡲ࡬ࡠࡶࡨࡷࡹࡥࡥࡷࡧࡱࡸࡸࠨᏫ"), datetime.now() - bstack1l11l1l111l_opy_)
                return # do not send this event with the bstack1l11l1ll1l1_opy_ bstack1l11l111lll_opy_
            elif (
                test_framework_state == bstack1llll11l1ll_opy_.TEST
                and test_hook_state == bstack1llll1l11l1_opy_.POST
                and not f.bstack1llll1ll1l1_opy_(instance, TestFramework.bstack1ll111lllll_opy_)
            ):
                self.logger.warning(bstack1lllll1_opy_ (u"ࠦࡩࡸ࡯ࡱࡲ࡬ࡲ࡬ࠦࡤࡶࡧࠣࡸࡴࠦ࡬ࡢࡥ࡮ࠤࡴ࡬ࠠࡳࡧࡶࡹࡱࡺࡳࠡࠤᏬ") + str(TestFramework.bstack1llll1ll1l1_opy_(instance, TestFramework.bstack1ll111lllll_opy_)) + bstack1lllll1_opy_ (u"ࠧࠨᏭ"))
                f.bstack1lllll1l11l_opy_(instance, bstack1l1l11llll1_opy_.bstack1l11ll11ll1_opy_, True)
                return # do not send this event bstack1l11l11ll11_opy_ bstack1l11ll1l111_opy_
            elif (
                f.get_state(instance, bstack1l1l11llll1_opy_.bstack1l11ll11ll1_opy_, False)
                and test_framework_state == bstack1llll11l1ll_opy_.LOG_REPORT
                and test_hook_state == bstack1llll1l11l1_opy_.POST
                and f.bstack1llll1ll1l1_opy_(instance, TestFramework.bstack1ll111lllll_opy_)
            ):
                self.logger.warning(bstack1lllll1_opy_ (u"ࠨࡩ࡯࡬ࡨࡧࡹ࡯࡮ࡨࠢࡗࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࡕࡷࡥࡹ࡫࠮ࡕࡇࡖࡘ࠱ࠦࡔࡦࡵࡷࡌࡴࡵ࡫ࡔࡶࡤࡸࡪ࠴ࡐࡐࡕࡗࠤࠧᏮ") + str(TestFramework.bstack1llll1ll1l1_opy_(instance, TestFramework.bstack1ll111lllll_opy_)) + bstack1lllll1_opy_ (u"ࠢࠣᏯ"))
                self.bstack1l11l11111l_opy_(f, instance, (bstack1llll11l1ll_opy_.TEST, bstack1llll1l11l1_opy_.POST), *args, **kwargs)
            bstack1l11llll11_opy_ = datetime.now()
            data = instance.data.copy()
            bstack1l11l1l11ll_opy_ = sorted(
                filter(lambda x: x.get(bstack1lllll1_opy_ (u"ࠣࡧࡹࡩࡳࡺ࡟ࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠦᏰ"), None), data.pop(bstack1lllll1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴࠤᏱ"), {}).values()),
                key=lambda x: x[bstack1lllll1_opy_ (u"ࠥࡩࡻ࡫࡮ࡵࡡࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹࠨᏲ")],
            )
            if bstack1lll11l111l_opy_.bstack1llll1111ll_opy_ in data:
                data.pop(bstack1lll11l111l_opy_.bstack1llll1111ll_opy_)
            data.update({bstack1lllll1_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡩ࡭ࡽࡺࡵࡳࡧࡶࠦᏳ"): bstack1l11l1l11ll_opy_})
            instance.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠧࡰࡳࡰࡰ࠽ࡸࡪࡹࡴࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࠥᏴ"), datetime.now() - bstack1l11llll11_opy_)
            bstack1l11llll11_opy_ = datetime.now()
            event_json = dumps(data, cls=bstack1l11ll1l1ll_opy_)
            instance.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠨࡪࡴࡱࡱ࠾ࡴࡴ࡟ࡢ࡮࡯ࡣࡹ࡫ࡳࡵࡡࡨࡺࡪࡴࡴࡴࠤᏵ"), datetime.now() - bstack1l11llll11_opy_)
            self.bstack1l11l111lll_opy_(instance, bstack1lllll111ll_opy_, event_json=event_json)
            instance.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠢࡰ࠳࠴ࡽ࠿ࡵ࡮ࡠࡣ࡯ࡰࡤࡺࡥࡴࡶࡢࡩࡻ࡫࡮ࡵࡵࠥ᏶"), datetime.now() - bstack1l11l1l111l_opy_)
    def bstack1lll1l1lll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack11l11l1111_opy_ import bstack1lllllllll1_opy_
        bstack1ll1l1l1111_opy_ = bstack1lllllllll1_opy_.bstack1ll11111ll1_opy_(EVENTS.bstack1111ll11ll_opy_.value)
        self.bstack1l11l11l1l1_opy_.bstack1lll1llll1l_opy_(instance, f, bstack1lllll111ll_opy_, *args, **kwargs)
        bstack1lllllllll1_opy_.end(EVENTS.bstack1111ll11ll_opy_.value, bstack1ll1l1l1111_opy_ + bstack1lllll1_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣ᏷"), bstack1ll1l1l1111_opy_ + bstack1lllll1_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᏸ"), status=True, failure=None, test_name=None)
    def bstack1llll111l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        req = self.bstack1l11l11l1l1_opy_.bstack1lll1ll1ll1_opy_(instance, f, bstack1lllll111ll_opy_, *args, **kwargs)
        self.bstack1l11ll111ll_opy_(f, instance, req)
    @measure(event_name=EVENTS.bstack1l11ll111l1_opy_, stage=STAGE.bstack11l1l111l1_opy_)
    def bstack1l11ll111ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        req: structs.TestSessionEventRequest
    ):
        if not req:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠥࡗࡰ࡯ࡰࡱ࡫ࡱ࡫࡚ࠥࡥࡴࡶࡖࡩࡸࡹࡩࡰࡰࡈࡺࡪࡴࡴࠡࡩࡕࡔࡈࠦࡣࡢ࡮࡯࠾ࠥࡔ࡯ࠡࡸࡤࡰ࡮ࡪࠠࡳࡧࡴࡹࡪࡹࡴࠡࡦࡤࡸࡦࠨᏹ"))
            return
        bstack1l11llll11_opy_ = datetime.now()
        try:
            r = self.bstack1111111l1l_opy_.TestSessionEvent(req)
            instance.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡶࡩࡳࡪ࡟ࡵࡧࡶࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡥࡷࡧࡱࡸࠧᏺ"), datetime.now() - bstack1l11llll11_opy_)
            f.bstack1lllll1l11l_opy_(instance, self.bstack1l11l11l1l1_opy_.bstack1llll11llll_opy_, r.success)
            if not r.success:
                self.logger.info(bstack1lllll1_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢᏻ") + str(r) + bstack1lllll1_opy_ (u"ࠨࠢᏼ"))
        except grpc.RpcError as e:
            self.logger.error(bstack1lllll1_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧᏽ") + str(e) + bstack1lllll1_opy_ (u"ࠣࠤ᏾"))
            traceback.print_exc()
            raise e
    def bstack1l11l11l111_opy_(
        self,
        f: bstack1lllll1ll11_opy_,
        _driver: object,
        exec: Tuple[bstack1111111l11_opy_, str],
        _1l11l1ll1ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if not bstack1lllll1ll11_opy_.bstack1l1ll1lllll_opy_(method_name):
            return
        if f.bstack1l1lll111l1_opy_(*args) == bstack1lllll1ll11_opy_.bstack1l11l1l1l11_opy_:
            bstack1l11l1l111l_opy_ = datetime.now()
            screenshot = result.get(bstack1lllll1_opy_ (u"ࠤࡹࡥࡱࡻࡥࠣ᏿"), None) if isinstance(result, dict) else None
            if not isinstance(screenshot, str) or len(screenshot) <= 0:
                self.logger.warning(bstack1lllll1_opy_ (u"ࠥ࡭ࡳࡼࡡ࡭࡫ࡧࠤࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠡ࡫ࡰࡥ࡬࡫ࠠࡣࡣࡶࡩ࠻࠺ࠠࡴࡶࡵࠦ᐀"))
                return
            bstack1l1lllll1ll_opy_ = self.bstack1l11l1ll11l_opy_(instance)
            if bstack1l1lllll1ll_opy_:
                entry = bstack1ll1l1l1ll1_opy_(TestFramework.bstack1l11l1lllll_opy_, screenshot)
                self.bstack1ll11111l11_opy_(bstack1l1lllll1ll_opy_, [entry])
                instance.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠦࡴ࠷࠱ࡺ࠼ࡲࡲࡤࡧࡦࡵࡧࡵࡣࡪࡾࡥࡤࡷࡷࡩࠧᐁ"), datetime.now() - bstack1l11l1l111l_opy_)
            else:
                self.logger.warning(bstack1lllll1_opy_ (u"ࠧࡻ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤࡹ࡫ࡳࡵࠢࡩࡳࡷࠦࡷࡩ࡫ࡦ࡬ࠥࡺࡨࡪࡵࠣࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠠࡸࡣࡶࠤࡹࡧ࡫ࡦࡰࠣࡦࡾࠦࡤࡳ࡫ࡹࡩࡷࡃࠠࡼࡿࠥᐂ").format(instance.ref()))
        event = {}
        bstack1l1lllll1ll_opy_ = self.bstack1l11l1ll11l_opy_(instance)
        if bstack1l1lllll1ll_opy_:
            self.bstack1l11l1111ll_opy_(event, bstack1l1lllll1ll_opy_)
            if event.get(bstack1lllll1_opy_ (u"ࠨ࡬ࡰࡩࡶࠦᐃ")):
                self.bstack1ll11111l11_opy_(bstack1l1lllll1ll_opy_, event[bstack1lllll1_opy_ (u"ࠢ࡭ࡱࡪࡷࠧᐄ")])
            else:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠ࡭ࡱࡪࡷࠥ࡬࡯ࡳࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠦࡥࡷࡧࡱࡸࠧᐅ"))
    @measure(event_name=EVENTS.bstack1l11l1lll1l_opy_, stage=STAGE.bstack11l1l111l1_opy_)
    def bstack1ll11111l11_opy_(
        self,
        bstack1l1lllll1ll_opy_: bstack1lll1l11l11_opy_,
        entries: List[bstack1ll1l1l1ll1_opy_],
    ):
        self.bstack1llll1lllll_opy_()
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(bstack1l1lllll1ll_opy_, TestFramework.bstack1111111ll1_opy_)
        req.execution_context.hash = str(bstack1l1lllll1ll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1l1lllll1ll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1l1lllll1ll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1l1lllll1ll_opy_, TestFramework.bstack1lll1ll1l1l_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1l1lllll1ll_opy_, TestFramework.bstack1lll1llllll_opy_)
            log_entry.uuid = TestFramework.get_state(bstack1l1lllll1ll_opy_, TestFramework.bstack1lll1lllll1_opy_)
            log_entry.test_framework_state = bstack1l1lllll1ll_opy_.state.name
            log_entry.message = entry.message.encode(bstack1lllll1_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᐆ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack1lllll1_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧᐇ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll1l1ll11l_opy_
                log_entry.file_path = entry.bstack11l1l11_opy_
        def bstack1ll11l1l111_opy_():
            bstack1l11llll11_opy_ = datetime.now()
            try:
                self.bstack1111111l1l_opy_.LogCreatedEvent(req)
                if entry.kind == TestFramework.bstack1l11l1lllll_opy_:
                    bstack1l1lllll1ll_opy_.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡶࡩࡳࡪ࡟࡭ࡱࡪࡣࡨࡸࡥࡢࡶࡨࡨࡤ࡫ࡶࡦࡰࡷࡣࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠣᐈ"), datetime.now() - bstack1l11llll11_opy_)
                elif entry.kind == TestFramework.bstack1l11l11llll_opy_:
                    bstack1l1lllll1ll_opy_.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡪࡴࡤࡠ࡮ࡲ࡫ࡤࡩࡲࡦࡣࡷࡩࡩࡥࡥࡷࡧࡱࡸࡤࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࠤᐉ"), datetime.now() - bstack1l11llll11_opy_)
                else:
                    bstack1l1lllll1ll_opy_.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡ࡯ࡳ࡬ࡥࡣࡳࡧࡤࡸࡪࡪ࡟ࡦࡸࡨࡲࡹࡥ࡬ࡰࡩࠥᐊ"), datetime.now() - bstack1l11llll11_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1lllll1_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧᐋ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11lllll_opy_.enqueue(bstack1ll11l1l111_opy_)
    @measure(event_name=EVENTS.bstack1l11ll1ll1l_opy_, stage=STAGE.bstack11l1l111l1_opy_)
    def bstack1l11l111lll_opy_(
        self,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_],
        event_json=None,
    ):
        self.bstack1llll1lllll_opy_()
        req = structs.TestFrameworkEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1111111ll1_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1ll1l1l_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1llllll_opy_)
        req.test_framework_state = bstack1lllll111ll_opy_[0].name
        req.test_hook_state = bstack1lllll111ll_opy_[1].name
        started_at = TestFramework.get_state(instance, TestFramework.bstack1ll1ll11l11_opy_, None)
        if started_at:
            req.started_at = started_at.isoformat()
        ended_at = TestFramework.get_state(instance, TestFramework.bstack1ll1111l11l_opy_, None)
        if ended_at:
            req.ended_at = ended_at.isoformat()
        req.uuid = instance.ref()
        req.event_json = (event_json if event_json else dumps(instance.data, cls=bstack1l11ll1l1ll_opy_)).encode(bstack1lllll1_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᐌ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        def bstack1ll11l1l111_opy_():
            bstack1l11llll11_opy_ = datetime.now()
            try:
                self.bstack1111111l1l_opy_.TestFrameworkEvent(req)
                instance.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡧࡱࡨࡤࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡥࡷࡧࡱࡸࠧᐍ"), datetime.now() - bstack1l11llll11_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1lllll1_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣᐎ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11lllll_opy_.enqueue(bstack1ll11l1l111_opy_)
    def bstack1l11l1ll11l_opy_(self, instance: bstack1111111l11_opy_):
        bstack1l11ll1l1l1_opy_ = TestFramework.bstack1l11l11ll1l_opy_(instance.context)
        for t in bstack1l11ll1l1l1_opy_:
            bstack1lll11ll111_opy_ = TestFramework.get_state(t, bstack1lll11l111l_opy_.bstack1llll1111ll_opy_, [])
            if any(instance is d[1] for d in bstack1lll11ll111_opy_):
                return t
    def bstack1l11ll11111_opy_(self, message):
        self.bstack1l11l1l1111_opy_(message + bstack1lllll1_opy_ (u"ࠦࡡࡴࠢᐏ"))
    def log_error(self, message):
        self.bstack1l11l1lll11_opy_(message + bstack1lllll1_opy_ (u"ࠧࡢ࡮ࠣᐐ"))
    def bstack1l11l1l1l1l_opy_(self, level, original_func):
        def bstack1l11ll1ll11_opy_(*args):
            return_value = original_func(*args)
            if not args or not isinstance(args[0], str) or not args[0].strip():
                return return_value
            message = args[0].strip()
            if bstack1lllll1_opy_ (u"ࠨࡅࡷࡧࡱࡸࡉ࡯ࡳࡱࡣࡷࡧ࡭࡫ࡲࡎࡱࡧࡹࡱ࡫ࠢᐑ") in message or bstack1lllll1_opy_ (u"ࠢ࡜ࡕࡇࡏࡈࡒࡉ࡞ࠤᐒ") in message or bstack1lllll1_opy_ (u"ࠣ࡝࡚ࡩࡧࡊࡲࡪࡸࡨࡶࡒࡵࡤࡶ࡮ࡨࡡࠧᐓ") in message:
                return return_value
            bstack1l11ll1l1l1_opy_ = TestFramework.bstack1l11ll11l1l_opy_()
            if not bstack1l11ll1l1l1_opy_:
                return return_value
            bstack1l1lllll1ll_opy_ = next(
                (
                    instance
                    for instance in bstack1l11ll1l1l1_opy_
                    if TestFramework.bstack1llll1ll1l1_opy_(instance, TestFramework.bstack1lll1lllll1_opy_)
                ),
                None,
            )
            if not bstack1l1lllll1ll_opy_:
                return return_value
            entry = bstack1ll1l1l1ll1_opy_(TestFramework.bstack1ll11111111_opy_, message, level)
            self.bstack1ll11111l11_opy_(bstack1l1lllll1ll_opy_, [entry])
            return return_value
        return bstack1l11ll1ll11_opy_
    def bstack1l11l111l11_opy_(self):
        def bstack1l11l11lll1_opy_(*args, **kwargs):
            try:
                self.bstack1l11ll1l11l_opy_(*args, **kwargs)
                if not args:
                    return
                message = bstack1lllll1_opy_ (u"ࠩࠣࠫᐔ").join(str(arg) for arg in args)
                if not message.strip():
                    return
                if bstack1lllll1_opy_ (u"ࠥࡉࡻ࡫࡮ࡵࡆ࡬ࡷࡵࡧࡴࡤࡪࡨࡶࡒࡵࡤࡶ࡮ࡨࠦᐕ") in message:
                    return
                bstack1l11ll1l1l1_opy_ = TestFramework.bstack1l11ll11l1l_opy_()
                if not bstack1l11ll1l1l1_opy_:
                    return
                bstack1l1lllll1ll_opy_ = next(
                    (
                        instance
                        for instance in bstack1l11ll1l1l1_opy_
                        if TestFramework.bstack1llll1ll1l1_opy_(instance, TestFramework.bstack1lll1lllll1_opy_)
                    ),
                    None,
                )
                if not bstack1l1lllll1ll_opy_:
                    return
                entry = bstack1ll1l1l1ll1_opy_(TestFramework.bstack1ll11111111_opy_, message, bstack1l1l11llll1_opy_.bstack1l11l111l1l_opy_)
                self.bstack1ll11111l11_opy_(bstack1l1lllll1ll_opy_, [entry])
            except Exception as e:
                try:
                    self.bstack1l11ll1l11l_opy_(bstack1lll1lll11l_opy_ (u"ࠦࡠࡋࡶࡦࡰࡷࡈ࡮ࡹࡰࡢࡶࡦ࡬ࡪࡸࡍࡰࡦࡸࡰࡪࡣࠠࡍࡱࡪࠤࡨࡧࡰࡵࡷࡵࡩࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡥࡾࠤᐖ"))
                except:
                    pass
        return bstack1l11l11lll1_opy_
    def bstack1l11l1111ll_opy_(self, event: dict, instance=None) -> None:
        global _1ll11l11l11_opy_
        levels = [bstack1lllll1_opy_ (u"࡚ࠧࡥࡴࡶࡏࡩࡻ࡫࡬ࠣᐗ"), bstack1lllll1_opy_ (u"ࠨࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࠥᐘ")]
        bstack1l11l1l1ll1_opy_ = bstack1lllll1_opy_ (u"ࠢࠣᐙ")
        if instance is not None:
            try:
                bstack1l11l1l1ll1_opy_ = TestFramework.get_state(instance, TestFramework.bstack1lll1lllll1_opy_)
            except Exception as e:
                self.logger.warning(bstack1lllll1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡷࡸ࡭ࡩࠦࡦࡳࡱࡰࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࠨᐚ").format(e))
        bstack1l11l111ll1_opy_ = []
        try:
            for level in levels:
                platform_index = os.environ[bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩᐛ")]
                bstack1ll11l1llll_opy_ = os.path.join(bstack1ll11l1111l_opy_, (bstack1ll11ll11ll_opy_ + str(platform_index)), level)
                if not os.path.isdir(bstack1ll11l1llll_opy_):
                    self.logger.debug(bstack1lllll1_opy_ (u"ࠥࡈ࡮ࡸࡥࡤࡶࡲࡶࡾࠦ࡮ࡰࡶࠣࡴࡷ࡫ࡳࡦࡰࡷࠤ࡫ࡵࡲࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫࡚ࠥࡥࡴࡶࠣࡥࡳࡪࠠࡃࡷ࡬ࡰࡩࠦ࡬ࡦࡸࡨࡰࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡿࢂࠨᐜ").format(bstack1ll11l1llll_opy_))
                    continue
                file_names = os.listdir(bstack1ll11l1llll_opy_)
                for file_name in file_names:
                    file_path = os.path.join(bstack1ll11l1llll_opy_, file_name)
                    abs_path = os.path.abspath(file_path)
                    if abs_path in _1ll11l11l11_opy_:
                        self.logger.info(bstack1lllll1_opy_ (u"ࠦࡕࡧࡴࡩࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡴࡷࡵࡣࡦࡵࡶࡩࡩࠦࡻࡾࠤᐝ").format(abs_path))
                        continue
                    if os.path.isfile(file_path):
                        try:
                            bstack1l11l1llll1_opy_ = os.path.getmtime(file_path)
                            timestamp = datetime.fromtimestamp(bstack1l11l1llll1_opy_, tz=timezone.utc).isoformat()
                            file_size = os.path.getsize(file_path)
                            if level == bstack1lllll1_opy_ (u"࡚ࠧࡥࡴࡶࡏࡩࡻ࡫࡬ࠣᐞ"):
                                entry = bstack1ll1l1l1ll1_opy_(
                                    kind=bstack1lllll1_opy_ (u"ࠨࡔࡆࡕࡗࡣࡆ࡚ࡔࡂࡅࡋࡑࡊࡔࡔࠣᐟ"),
                                    message=bstack1lllll1_opy_ (u"ࠢࠣᐠ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1ll1l1ll11l_opy_=file_size,
                                    bstack1ll1l11l1ll_opy_=bstack1lllll1_opy_ (u"ࠣࡏࡄࡒ࡚ࡇࡌࡠࡗࡓࡐࡔࡇࡄࠣᐡ"),
                                    bstack11l1l11_opy_=os.path.abspath(file_path),
                                    bstack11ll1l1lll_opy_=bstack1l11l1l1ll1_opy_
                                )
                            elif level == bstack1lllll1_opy_ (u"ࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠨᐢ"):
                                entry = bstack1ll1l1l1ll1_opy_(
                                    kind=bstack1lllll1_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧᐣ"),
                                    message=bstack1lllll1_opy_ (u"ࠦࠧᐤ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1ll1l1ll11l_opy_=file_size,
                                    bstack1ll1l11l1ll_opy_=bstack1lllll1_opy_ (u"ࠧࡓࡁࡏࡗࡄࡐࡤ࡛ࡐࡍࡑࡄࡈࠧᐥ"),
                                    bstack11l1l11_opy_=os.path.abspath(file_path),
                                    bstack1ll1111l111_opy_=bstack1l11l1l1ll1_opy_
                                )
                            bstack1l11l111ll1_opy_.append(entry)
                            _1ll11l11l11_opy_.add(abs_path)
                        except Exception as bstack1l11ll1111l_opy_:
                            self.logger.error(bstack1lllll1_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡵࡥ࡮ࡹࡥࡥࠢࡺ࡬ࡪࡴࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴࠢࡾࢁࠧᐦ").format(bstack1l11ll1111l_opy_))
        except Exception as e:
            self.logger.error(bstack1lllll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡶࡦ࡯ࡳࡦࡦࠣࡻ࡭࡫࡮ࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡿࢂࠨᐧ").format(e))
        event[bstack1lllll1_opy_ (u"ࠣ࡮ࡲ࡫ࡸࠨᐨ")] = bstack1l11l111ll1_opy_
class bstack1l11ll1l1ll_opy_(JSONEncoder):
    def __init__(self, **kwargs):
        self.bstack1l11l1l11l1_opy_ = set()
        kwargs[bstack1lllll1_opy_ (u"ࠤࡶ࡯࡮ࡶ࡫ࡦࡻࡶࠦᐩ")] = True
        super().__init__(**kwargs)
    def default(self, obj):
        return bstack1l11l1111l1_opy_(obj, self.bstack1l11l1l11l1_opy_)
def bstack1l11l11l1ll_opy_(obj):
    return isinstance(obj, (str, int, float, bool, type(None)))
def bstack1l11l1111l1_opy_(obj, bstack1l11l1l11l1_opy_=None, max_depth=3):
    if bstack1l11l1l11l1_opy_ is None:
        bstack1l11l1l11l1_opy_ = set()
    if id(obj) in bstack1l11l1l11l1_opy_ or max_depth <= 0:
        return None
    max_depth -= 1
    bstack1l11l1l11l1_opy_.add(id(obj))
    if isinstance(obj, datetime):
        return obj.isoformat()
    bstack1l11l1ll111_opy_ = TestFramework.bstack1ll1l1ll1ll_opy_(obj)
    bstack1l11l1l1lll_opy_ = next((k.lower() in bstack1l11l1ll111_opy_.lower() for k in bstack1l11l11l11l_opy_.keys()), None)
    if bstack1l11l1l1lll_opy_:
        obj = TestFramework.bstack1ll1l11l111_opy_(obj, bstack1l11l11l11l_opy_[bstack1l11l1l1lll_opy_])
    if not isinstance(obj, dict):
        keys = []
        if hasattr(obj, bstack1lllll1_opy_ (u"ࠥࡣࡤࡹ࡬ࡰࡶࡶࡣࡤࠨᐪ")):
            keys = getattr(obj, bstack1lllll1_opy_ (u"ࠦࡤࡥࡳ࡭ࡱࡷࡷࡤࡥࠢᐫ"), [])
        elif hasattr(obj, bstack1lllll1_opy_ (u"ࠧࡥ࡟ࡥ࡫ࡦࡸࡤࡥࠢᐬ")):
            keys = getattr(obj, bstack1lllll1_opy_ (u"ࠨ࡟ࡠࡦ࡬ࡧࡹࡥ࡟ࠣᐭ"), {}).keys()
        else:
            keys = dir(obj)
        obj = {k: getattr(obj, k, None) for k in keys if not str(k).startswith(bstack1lllll1_opy_ (u"ࠢࡠࠤᐮ"))}
        if not obj and bstack1l11l1ll111_opy_ == bstack1lllll1_opy_ (u"ࠣࡲࡤࡸ࡭ࡲࡩࡣ࠰ࡓࡳࡸ࡯ࡸࡑࡣࡷ࡬ࠧᐯ"):
            obj = {bstack1lllll1_opy_ (u"ࠤࡳࡥࡹ࡮ࠢᐰ"): str(obj)}
    result = {}
    for key, value in obj.items():
        if not bstack1l11l11l1ll_opy_(key) or str(key).startswith(bstack1lllll1_opy_ (u"ࠥࡣࠧᐱ")):
            continue
        if value is not None and bstack1l11l11l1ll_opy_(value):
            result[key] = value
        elif isinstance(value, dict):
            r = bstack1l11l1111l1_opy_(value, bstack1l11l1l11l1_opy_, max_depth)
            if r is not None:
                result[key] = r
        elif isinstance(value, (list, tuple, set, frozenset)):
            result[key] = list(filter(None, [bstack1l11l1111l1_opy_(o, bstack1l11l1l11l1_opy_, max_depth) for o in value]))
    return result or None