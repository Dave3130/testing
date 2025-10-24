# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
from datetime import datetime, timezone
import os
import builtins
from pathlib import Path
from typing import Any, Tuple, Callable, List
from browserstack_sdk.sdk_cli.bstack1llll11ll1l_opy_ import bstack1llllll1l1l_opy_, bstack1llllll111l_opy_, bstack1llll1l111l_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1lll_opy_ import bstack1llll1llll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l1l1l_opy_ import bstack1lll11l1l11_opy_
from browserstack_sdk.sdk_cli.bstack1111111l11_opy_ import bstack1llll1l11l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll11l11l_opy_, bstack1lll1l11111_opy_, bstack1lll11llll1_opy_, bstack1ll111ll111_opy_
from json import dumps, JSONEncoder
import grpc
from browserstack_sdk import sdk_pb2 as structs
import sys
import traceback
import time
import json
from bstack_utils.helper import bstack1lll1ll111l_opy_, bstack1l1llll1111_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
bstack1l111lll11l_opy_ = [bstack1l1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᏅ"), bstack1l1_opy_ (u"ࠣࡲࡤࡶࡪࡴࡴࠣᏆ"), bstack1l1_opy_ (u"ࠤࡦࡳࡳ࡬ࡩࡨࠤᏇ"), bstack1l1_opy_ (u"ࠥࡷࡪࡹࡳࡪࡱࡱࠦᏈ"), bstack1l1_opy_ (u"ࠦࡵࡧࡴࡩࠤᏉ")]
bstack1ll11lll11l_opy_ = bstack1l1llll1111_opy_()
bstack1ll1111llll_opy_ = bstack1l1_opy_ (u"࡛ࠧࡰ࡭ࡱࡤࡨࡪࡪࡁࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶ࠱ࠧᏊ")
bstack1l111llllll_opy_ = {
    bstack1l1_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡰࡺࡶ࡫ࡳࡳ࠴ࡉࡵࡧࡰࠦᏋ"): bstack1l111lll11l_opy_,
    bstack1l1_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡱࡻࡷ࡬ࡴࡴ࠮ࡑࡣࡦ࡯ࡦ࡭ࡥࠣᏌ"): bstack1l111lll11l_opy_,
    bstack1l1_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡲࡼࡸ࡭ࡵ࡮࠯ࡏࡲࡨࡺࡲࡥࠣᏍ"): bstack1l111lll11l_opy_,
    bstack1l1_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡳࡽࡹ࡮࡯࡯࠰ࡆࡰࡦࡹࡳࠣᏎ"): bstack1l111lll11l_opy_,
    bstack1l1_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡴࡾࡺࡨࡰࡰ࠱ࡊࡺࡴࡣࡵ࡫ࡲࡲࠧᏏ"): bstack1l111lll11l_opy_
    + [
        bstack1l1_opy_ (u"ࠦࡴࡸࡩࡨ࡫ࡱࡥࡱࡴࡡ࡮ࡧࠥᏐ"),
        bstack1l1_opy_ (u"ࠧࡱࡥࡺࡹࡲࡶࡩࡹࠢᏑ"),
        bstack1l1_opy_ (u"ࠨࡦࡪࡺࡷࡹࡷ࡫ࡩ࡯ࡨࡲࠦᏒ"),
        bstack1l1_opy_ (u"ࠢ࡬ࡧࡼࡻࡴࡸࡤࡴࠤᏓ"),
        bstack1l1_opy_ (u"ࠣࡥࡤࡰࡱࡹࡰࡦࡥࠥᏔ"),
        bstack1l1_opy_ (u"ࠤࡦࡥࡱࡲ࡯ࡣ࡬ࠥᏕ"),
        bstack1l1_opy_ (u"ࠥࡷࡹࡧࡲࡵࠤᏖ"),
        bstack1l1_opy_ (u"ࠦࡸࡺ࡯ࡱࠤᏗ"),
        bstack1l1_opy_ (u"ࠧࡪࡵࡳࡣࡷ࡭ࡴࡴࠢᏘ"),
        bstack1l1_opy_ (u"ࠨࡷࡩࡧࡱࠦᏙ"),
    ],
    bstack1l1_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮࡮ࡣ࡬ࡲ࠳࡙ࡥࡴࡵ࡬ࡳࡳࠨᏚ"): [bstack1l1_opy_ (u"ࠣࡵࡷࡥࡷࡺࡰࡢࡶ࡫ࠦᏛ"), bstack1l1_opy_ (u"ࠤࡷࡩࡸࡺࡳࡧࡣ࡬ࡰࡪࡪࠢᏜ"), bstack1l1_opy_ (u"ࠥࡸࡪࡹࡴࡴࡥࡲࡰࡱ࡫ࡣࡵࡧࡧࠦᏝ"), bstack1l1_opy_ (u"ࠦ࡮ࡺࡥ࡮ࡵࠥᏞ")],
    bstack1l1_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡩ࡯࡯ࡨ࡬࡫࠳ࡉ࡯࡯ࡨ࡬࡫ࠧᏟ"): [bstack1l1_opy_ (u"ࠨࡩ࡯ࡸࡲࡧࡦࡺࡩࡰࡰࡢࡴࡦࡸࡡ࡮ࡵࠥᏠ"), bstack1l1_opy_ (u"ࠢࡢࡴࡪࡷࠧᏡ")],
    bstack1l1_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡨ࡬ࡼࡹࡻࡲࡦࡵ࠱ࡊ࡮ࡾࡴࡶࡴࡨࡈࡪ࡬ࠢᏢ"): [bstack1l1_opy_ (u"ࠤࡶࡧࡴࡶࡥࠣᏣ"), bstack1l1_opy_ (u"ࠥࡥࡷ࡭࡮ࡢ࡯ࡨࠦᏤ"), bstack1l1_opy_ (u"ࠦ࡫ࡻ࡮ࡤࠤᏥ"), bstack1l1_opy_ (u"ࠧࡶࡡࡳࡣࡰࡷࠧᏦ"), bstack1l1_opy_ (u"ࠨࡵ࡯࡫ࡷࡸࡪࡹࡴࠣᏧ"), bstack1l1_opy_ (u"ࠢࡪࡦࡶࠦᏨ")],
    bstack1l1_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡨ࡬ࡼࡹࡻࡲࡦࡵ࠱ࡗࡺࡨࡒࡦࡳࡸࡩࡸࡺࠢᏩ"): [bstack1l1_opy_ (u"ࠤࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࠢᏪ"), bstack1l1_opy_ (u"ࠥࡴࡦࡸࡡ࡮ࠤᏫ"), bstack1l1_opy_ (u"ࠦࡵࡧࡲࡢ࡯ࡢ࡭ࡳࡪࡥࡹࠤᏬ")],
    bstack1l1_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡸࡵ࡯ࡰࡨࡶ࠳ࡉࡡ࡭࡮ࡌࡲ࡫ࡵࠢᏭ"): [bstack1l1_opy_ (u"ࠨࡷࡩࡧࡱࠦᏮ"), bstack1l1_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࠢᏯ")],
    bstack1l1_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯࡯ࡤࡶࡰ࠴ࡳࡵࡴࡸࡧࡹࡻࡲࡦࡵ࠱ࡒࡴࡪࡥࡌࡧࡼࡻࡴࡸࡤࡴࠤᏰ"): [bstack1l1_opy_ (u"ࠤࡱࡳࡩ࡫ࠢᏱ"), bstack1l1_opy_ (u"ࠥࡴࡦࡸࡥ࡯ࡶࠥᏲ")],
    bstack1l1_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡲࡧࡲ࡬࠰ࡶࡸࡷࡻࡣࡵࡷࡵࡩࡸ࠴ࡍࡢࡴ࡮ࠦᏳ"): [bstack1l1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᏴ"), bstack1l1_opy_ (u"ࠨࡡࡳࡩࡶࠦᏵ"), bstack1l1_opy_ (u"ࠢ࡬ࡹࡤࡶ࡬ࡹࠢ᏶")],
}
_1l1llll1lll_opy_ = set()
class bstack1l11lll1111_opy_(bstack1llll1llll1_opy_):
    bstack1l11l1l11ll_opy_ = bstack1l1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡤࡦࡨࡨࡶࡷ࡫ࡤࠣ᏷")
    bstack1l11l111111_opy_ = bstack1l1_opy_ (u"ࠤࡌࡒࡋࡕࠢᏸ")
    bstack1l11l1l1l1l_opy_ = bstack1l1_opy_ (u"ࠥࡉࡗࡘࡏࡓࠤᏹ")
    bstack1l11l1ll111_opy_: Callable
    bstack1l111lll1l1_opy_: Callable
    def __init__(self, bstack1l1l1llll11_opy_, bstack1ll1ll1llll_opy_):
        super().__init__()
        self.bstack1l11l111lll_opy_ = bstack1ll1ll1llll_opy_
        if os.getenv(bstack1l1_opy_ (u"ࠦࡘࡊࡋࡠࡅࡏࡍࡤࡌࡌࡂࡉࡢࡓ࠶࠷࡙ࠣᏺ"), bstack1l1_opy_ (u"ࠧ࠷ࠢᏻ")) != bstack1l1_opy_ (u"ࠨ࠱ࠣᏼ") or not self.is_enabled():
            self.logger.warning(bstack1l1_opy_ (u"ࠢࠣᏽ") + str(self.__class__.__name__) + bstack1l1_opy_ (u"ࠣࠢࡧ࡭ࡸࡧࡢ࡭ࡧࡧࠦ᏾"))
            return
        TestFramework.bstack1llll1ll1l1_opy_((bstack1llll11l11l_opy_.TEST, bstack1lll11llll1_opy_.PRE), self.bstack1lll1l11lll_opy_)
        TestFramework.bstack1llll1ll1l1_opy_((bstack1llll11l11l_opy_.TEST, bstack1lll11llll1_opy_.POST), self.bstack1lll11ll1l1_opy_)
        for event in bstack1llll11l11l_opy_:
            for state in bstack1lll11llll1_opy_:
                TestFramework.bstack1llll1ll1l1_opy_((event, state), self.bstack1l11l11111l_opy_)
        bstack1l1l1llll11_opy_.bstack1llll1ll1l1_opy_((bstack1llllll111l_opy_.bstack1lllllll111_opy_, bstack1llll1l111l_opy_.POST), self.bstack1l11l1l1ll1_opy_)
        self.bstack1l11l1ll111_opy_ = sys.stdout.write
        sys.stdout.write = self.bstack1l111llll11_opy_(bstack1l11lll1111_opy_.bstack1l11l111111_opy_, self.bstack1l11l1ll111_opy_)
        self.bstack1l111lll1l1_opy_ = sys.stderr.write
        sys.stderr.write = self.bstack1l111llll11_opy_(bstack1l11lll1111_opy_.bstack1l11l1l1l1l_opy_, self.bstack1l111lll1l1_opy_)
        self.bstack1l11l111l11_opy_ = builtins.print
        builtins.print = self.bstack1l111llll1l_opy_()
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l11111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11111_opy_,
        bstack1lllll1l1l1_opy_: Tuple[bstack1llll11l11l_opy_, bstack1lll11llll1_opy_],
        *args,
        **kwargs,
    ):
        if f.bstack1l1lllll1l1_opy_() and instance:
            bstack1l11l11lll1_opy_ = datetime.now()
            test_framework_state, test_hook_state = bstack1lllll1l1l1_opy_
            if test_framework_state == bstack1llll11l11l_opy_.SETUP_FIXTURE:
                return
            elif test_framework_state == bstack1llll11l11l_opy_.LOG:
                bstack1l1ll111l_opy_ = datetime.now()
                entries = f.bstack1l1lll1lll1_opy_(instance, bstack1lllll1l1l1_opy_)
                if entries:
                    self.bstack1ll1111ll1l_opy_(instance, entries)
                    instance.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡧࡱࡨࡤࡲ࡯ࡨࡡࡦࡶࡪࡧࡴࡦࡦࡢࡩࡻ࡫࡮ࡵࠤ᏿"), datetime.now() - bstack1l1ll111l_opy_)
                    f.bstack1ll1l1l1l11_opy_(instance, bstack1lllll1l1l1_opy_)
                instance.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠥࡳ࠶࠷ࡹ࠻ࡱࡱࡣࡦࡲ࡬ࡠࡶࡨࡷࡹࡥࡥࡷࡧࡱࡸࡸࠨ᐀"), datetime.now() - bstack1l11l11lll1_opy_)
                return # do not send this event with the bstack1l11l11l1l1_opy_ bstack1l11l1l1l11_opy_
            elif (
                test_framework_state == bstack1llll11l11l_opy_.TEST
                and test_hook_state == bstack1lll11llll1_opy_.POST
                and not f.bstack1llllllll11_opy_(instance, TestFramework.bstack1l1lllll11l_opy_)
            ):
                self.logger.warning(bstack1l1_opy_ (u"ࠦࡩࡸ࡯ࡱࡲ࡬ࡲ࡬ࠦࡤࡶࡧࠣࡸࡴࠦ࡬ࡢࡥ࡮ࠤࡴ࡬ࠠࡳࡧࡶࡹࡱࡺࡳࠡࠤᐁ") + str(TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1l1lllll11l_opy_)) + bstack1l1_opy_ (u"ࠧࠨᐂ"))
                f.bstack1llll1l1lll_opy_(instance, bstack1l11lll1111_opy_.bstack1l11l1l11ll_opy_, True)
                return # do not send this event bstack1l11l1l111l_opy_ bstack1l11ll1111l_opy_
            elif (
                f.get_state(instance, bstack1l11lll1111_opy_.bstack1l11l1l11ll_opy_, False)
                and test_framework_state == bstack1llll11l11l_opy_.LOG_REPORT
                and test_hook_state == bstack1lll11llll1_opy_.POST
                and f.bstack1llllllll11_opy_(instance, TestFramework.bstack1l1lllll11l_opy_)
            ):
                self.logger.warning(bstack1l1_opy_ (u"ࠨࡩ࡯࡬ࡨࡧࡹ࡯࡮ࡨࠢࡗࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࡕࡷࡥࡹ࡫࠮ࡕࡇࡖࡘ࠱ࠦࡔࡦࡵࡷࡌࡴࡵ࡫ࡔࡶࡤࡸࡪ࠴ࡐࡐࡕࡗࠤࠧᐃ") + str(TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1l1lllll11l_opy_)) + bstack1l1_opy_ (u"ࠢࠣᐄ"))
                self.bstack1l11l11111l_opy_(f, instance, (bstack1llll11l11l_opy_.TEST, bstack1lll11llll1_opy_.POST), *args, **kwargs)
            bstack1l1ll111l_opy_ = datetime.now()
            data = instance.data.copy()
            bstack1l11l1111ll_opy_ = sorted(
                filter(lambda x: x.get(bstack1l1_opy_ (u"ࠣࡧࡹࡩࡳࡺ࡟ࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠦᐅ"), None), data.pop(bstack1l1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴࠤᐆ"), {}).values()),
                key=lambda x: x[bstack1l1_opy_ (u"ࠥࡩࡻ࡫࡮ࡵࡡࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹࠨᐇ")],
            )
            if bstack1lll11l1l11_opy_.bstack1llll1111l1_opy_ in data:
                data.pop(bstack1lll11l1l11_opy_.bstack1llll1111l1_opy_)
            data.update({bstack1l1_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡩ࡭ࡽࡺࡵࡳࡧࡶࠦᐈ"): bstack1l11l1111ll_opy_})
            instance.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠧࡰࡳࡰࡰ࠽ࡸࡪࡹࡴࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࠥᐉ"), datetime.now() - bstack1l1ll111l_opy_)
            bstack1l1ll111l_opy_ = datetime.now()
            event_json = dumps(data, cls=bstack1l11l11ll1l_opy_)
            instance.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠨࡪࡴࡱࡱ࠾ࡴࡴ࡟ࡢ࡮࡯ࡣࡹ࡫ࡳࡵࡡࡨࡺࡪࡴࡴࡴࠤᐊ"), datetime.now() - bstack1l1ll111l_opy_)
            self.bstack1l11l1l1l11_opy_(instance, bstack1lllll1l1l1_opy_, event_json=event_json)
            instance.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠢࡰ࠳࠴ࡽ࠿ࡵ࡮ࡠࡣ࡯ࡰࡤࡺࡥࡴࡶࡢࡩࡻ࡫࡮ࡵࡵࠥᐋ"), datetime.now() - bstack1l11l11lll1_opy_)
    def bstack1lll1l11lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11111_opy_,
        bstack1lllll1l1l1_opy_: Tuple[bstack1llll11l11l_opy_, bstack1lll11llll1_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack111l11l11_opy_ import bstack1lllllll11l_opy_
        bstack1ll11ll1lll_opy_ = bstack1lllllll11l_opy_.bstack1ll1l1l1lll_opy_(EVENTS.bstack11ll1111l_opy_.value)
        self.bstack1l11l111lll_opy_.bstack1lll1lll1ll_opy_(instance, f, bstack1lllll1l1l1_opy_, *args, **kwargs)
        bstack1lllllll11l_opy_.end(EVENTS.bstack11ll1111l_opy_.value, bstack1ll11ll1lll_opy_ + bstack1l1_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᐌ"), bstack1ll11ll1lll_opy_ + bstack1l1_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᐍ"), status=True, failure=None, test_name=None)
    def bstack1lll11ll1l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11111_opy_,
        bstack1lllll1l1l1_opy_: Tuple[bstack1llll11l11l_opy_, bstack1lll11llll1_opy_],
        *args,
        **kwargs,
    ):
        req = self.bstack1l11l111lll_opy_.bstack1lll1ll1lll_opy_(instance, f, bstack1lllll1l1l1_opy_, *args, **kwargs)
        self.bstack1l11l11l1ll_opy_(f, instance, req)
    @measure(event_name=EVENTS.bstack1l11l1l1111_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
    def bstack1l11l11l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11111_opy_,
        req: structs.TestSessionEventRequest
    ):
        if not req:
            self.logger.debug(bstack1l1_opy_ (u"ࠥࡗࡰ࡯ࡰࡱ࡫ࡱ࡫࡚ࠥࡥࡴࡶࡖࡩࡸࡹࡩࡰࡰࡈࡺࡪࡴࡴࠡࡩࡕࡔࡈࠦࡣࡢ࡮࡯࠾ࠥࡔ࡯ࠡࡸࡤࡰ࡮ࡪࠠࡳࡧࡴࡹࡪࡹࡴࠡࡦࡤࡸࡦࠨᐎ"))
            return
        bstack1l1ll111l_opy_ = datetime.now()
        try:
            r = self.bstack1llll1l11ll_opy_.TestSessionEvent(req)
            instance.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡶࡩࡳࡪ࡟ࡵࡧࡶࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡥࡷࡧࡱࡸࠧᐏ"), datetime.now() - bstack1l1ll111l_opy_)
            f.bstack1llll1l1lll_opy_(instance, self.bstack1l11l111lll_opy_.bstack1lll1l111ll_opy_, r.success)
            if not r.success:
                self.logger.info(bstack1l1_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢᐐ") + str(r) + bstack1l1_opy_ (u"ࠨࠢᐑ"))
        except grpc.RpcError as e:
            self.logger.error(bstack1l1_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧᐒ") + str(e) + bstack1l1_opy_ (u"ࠣࠤᐓ"))
            traceback.print_exc()
            raise e
    def bstack1l11l1l1ll1_opy_(
        self,
        f: bstack1llll1l11l1_opy_,
        _driver: object,
        exec: Tuple[bstack1llllll1l1l_opy_, str],
        _1l11l111l1l_opy_: Tuple[bstack1llllll111l_opy_, bstack1llll1l111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if not bstack1llll1l11l1_opy_.bstack1l1ll1ll1l1_opy_(method_name):
            return
        if f.bstack1l1lll11ll1_opy_(*args) == bstack1llll1l11l1_opy_.bstack1l11ll111ll_opy_:
            bstack1l11l11lll1_opy_ = datetime.now()
            screenshot = result.get(bstack1l1_opy_ (u"ࠤࡹࡥࡱࡻࡥࠣᐔ"), None) if isinstance(result, dict) else None
            if not isinstance(screenshot, str) or len(screenshot) <= 0:
                self.logger.warning(bstack1l1_opy_ (u"ࠥ࡭ࡳࡼࡡ࡭࡫ࡧࠤࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠡ࡫ࡰࡥ࡬࡫ࠠࡣࡣࡶࡩ࠻࠺ࠠࡴࡶࡵࠦᐕ"))
                return
            bstack1ll111lllll_opy_ = self.bstack1l11l1ll1l1_opy_(instance)
            if bstack1ll111lllll_opy_:
                entry = bstack1ll111ll111_opy_(TestFramework.bstack1l11l11l111_opy_, screenshot)
                self.bstack1ll1111ll1l_opy_(bstack1ll111lllll_opy_, [entry])
                instance.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠦࡴ࠷࠱ࡺ࠼ࡲࡲࡤࡧࡦࡵࡧࡵࡣࡪࡾࡥࡤࡷࡷࡩࠧᐖ"), datetime.now() - bstack1l11l11lll1_opy_)
            else:
                self.logger.warning(bstack1l1_opy_ (u"ࠧࡻ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤࡹ࡫ࡳࡵࠢࡩࡳࡷࠦࡷࡩ࡫ࡦ࡬ࠥࡺࡨࡪࡵࠣࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠠࡸࡣࡶࠤࡹࡧ࡫ࡦࡰࠣࡦࡾࠦࡤࡳ࡫ࡹࡩࡷࡃࠠࡼࡿࠥᐗ").format(instance.ref()))
        event = {}
        bstack1ll111lllll_opy_ = self.bstack1l11l1ll1l1_opy_(instance)
        if bstack1ll111lllll_opy_:
            self.bstack1l11l11ll11_opy_(event, bstack1ll111lllll_opy_)
            if event.get(bstack1l1_opy_ (u"ࠨ࡬ࡰࡩࡶࠦᐘ")):
                self.bstack1ll1111ll1l_opy_(bstack1ll111lllll_opy_, event[bstack1l1_opy_ (u"ࠢ࡭ࡱࡪࡷࠧᐙ")])
            else:
                self.logger.debug(bstack1l1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠ࡭ࡱࡪࡷࠥ࡬࡯ࡳࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠦࡥࡷࡧࡱࡸࠧᐚ"))
    @measure(event_name=EVENTS.bstack1l11l1l11l1_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
    def bstack1ll1111ll1l_opy_(
        self,
        bstack1ll111lllll_opy_: bstack1lll1l11111_opy_,
        entries: List[bstack1ll111ll111_opy_],
    ):
        self.bstack1llll1l1l1l_opy_()
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(bstack1ll111lllll_opy_, TestFramework.bstack1lllll1l11l_opy_)
        req.execution_context.hash = str(bstack1ll111lllll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll111lllll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll111lllll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll111lllll_opy_, TestFramework.bstack1lll1l1111l_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll111lllll_opy_, TestFramework.bstack1lll1ll1l11_opy_)
            log_entry.uuid = TestFramework.get_state(bstack1ll111lllll_opy_, TestFramework.bstack1llll111ll1_opy_)
            log_entry.test_framework_state = bstack1ll111lllll_opy_.state.name
            log_entry.message = entry.message.encode(bstack1l1_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᐛ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack1l1_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧᐜ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll1l1lll11_opy_
                log_entry.file_path = entry.bstack11l111l_opy_
        def bstack1ll1l1l1l1l_opy_():
            bstack1l1ll111l_opy_ = datetime.now()
            try:
                self.bstack1llll1l11ll_opy_.LogCreatedEvent(req)
                if entry.kind == TestFramework.bstack1l11l11l111_opy_:
                    bstack1ll111lllll_opy_.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡶࡩࡳࡪ࡟࡭ࡱࡪࡣࡨࡸࡥࡢࡶࡨࡨࡤ࡫ࡶࡦࡰࡷࡣࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠣᐝ"), datetime.now() - bstack1l1ll111l_opy_)
                elif entry.kind == TestFramework.bstack1l11l1ll11l_opy_:
                    bstack1ll111lllll_opy_.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡪࡴࡤࡠ࡮ࡲ࡫ࡤࡩࡲࡦࡣࡷࡩࡩࡥࡥࡷࡧࡱࡸࡤࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࠤᐞ"), datetime.now() - bstack1l1ll111l_opy_)
                else:
                    bstack1ll111lllll_opy_.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡ࡯ࡳ࡬ࡥࡣࡳࡧࡤࡸࡪࡪ࡟ࡦࡸࡨࡲࡹࡥ࡬ࡰࡩࠥᐟ"), datetime.now() - bstack1l1ll111l_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1l1_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧᐠ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11l1ll1_opy_.enqueue(bstack1ll1l1l1l1l_opy_)
    @measure(event_name=EVENTS.bstack1l11l1llll1_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
    def bstack1l11l1l1l11_opy_(
        self,
        instance: bstack1lll1l11111_opy_,
        bstack1lllll1l1l1_opy_: Tuple[bstack1llll11l11l_opy_, bstack1lll11llll1_opy_],
        event_json=None,
    ):
        self.bstack1llll1l1l1l_opy_()
        req = structs.TestFrameworkEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1lllll1l11l_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1l1111l_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1ll1l11_opy_)
        req.test_framework_state = bstack1lllll1l1l1_opy_[0].name
        req.test_hook_state = bstack1lllll1l1l1_opy_[1].name
        started_at = TestFramework.get_state(instance, TestFramework.bstack1ll11l1ll1l_opy_, None)
        if started_at:
            req.started_at = started_at.isoformat()
        ended_at = TestFramework.get_state(instance, TestFramework.bstack1l1lllllll1_opy_, None)
        if ended_at:
            req.ended_at = ended_at.isoformat()
        req.uuid = instance.ref()
        req.event_json = (event_json if event_json else dumps(instance.data, cls=bstack1l11l11ll1l_opy_)).encode(bstack1l1_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᐡ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        def bstack1ll1l1l1l1l_opy_():
            bstack1l1ll111l_opy_ = datetime.now()
            try:
                self.bstack1llll1l11ll_opy_.TestFrameworkEvent(req)
                instance.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡧࡱࡨࡤࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡥࡷࡧࡱࡸࠧᐢ"), datetime.now() - bstack1l1ll111l_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1l1_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣᐣ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11l1ll1_opy_.enqueue(bstack1ll1l1l1l1l_opy_)
    def bstack1l11l1ll1l1_opy_(self, instance: bstack1llllll1l1l_opy_):
        bstack1l11ll11111_opy_ = TestFramework.bstack1l11l1lll1l_opy_(instance.context)
        for t in bstack1l11ll11111_opy_:
            bstack1lll1111l11_opy_ = TestFramework.get_state(t, bstack1lll11l1l11_opy_.bstack1llll1111l1_opy_, [])
            if any(instance is d[1] for d in bstack1lll1111l11_opy_):
                return t
    def bstack1l11l1111l1_opy_(self, message):
        self.bstack1l11l1ll111_opy_(message + bstack1l1_opy_ (u"ࠦࡡࡴࠢᐤ"))
    def log_error(self, message):
        self.bstack1l111lll1l1_opy_(message + bstack1l1_opy_ (u"ࠧࡢ࡮ࠣᐥ"))
    def bstack1l111llll11_opy_(self, level, original_func):
        def bstack1l111lll111_opy_(*args):
            return_value = original_func(*args)
            if not args or not isinstance(args[0], str) or not args[0].strip():
                return return_value
            message = args[0].strip()
            if bstack1l1_opy_ (u"ࠨࡅࡷࡧࡱࡸࡉ࡯ࡳࡱࡣࡷࡧ࡭࡫ࡲࡎࡱࡧࡹࡱ࡫ࠢᐦ") in message or bstack1l1_opy_ (u"ࠢ࡜ࡕࡇࡏࡈࡒࡉ࡞ࠤᐧ") in message or bstack1l1_opy_ (u"ࠣ࡝࡚ࡩࡧࡊࡲࡪࡸࡨࡶࡒࡵࡤࡶ࡮ࡨࡡࠧᐨ") in message:
                return return_value
            bstack1l11ll11111_opy_ = TestFramework.bstack1l11l11llll_opy_()
            if not bstack1l11ll11111_opy_:
                return return_value
            bstack1ll111lllll_opy_ = next(
                (
                    instance
                    for instance in bstack1l11ll11111_opy_
                    if TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1llll111ll1_opy_)
                ),
                None,
            )
            if not bstack1ll111lllll_opy_:
                return return_value
            entry = bstack1ll111ll111_opy_(TestFramework.bstack1ll11111111_opy_, message, level)
            self.bstack1ll1111ll1l_opy_(bstack1ll111lllll_opy_, [entry])
            return return_value
        return bstack1l111lll111_opy_
    def bstack1l111llll1l_opy_(self):
        def bstack1l11l1lllll_opy_(*args, **kwargs):
            try:
                self.bstack1l11l111l11_opy_(*args, **kwargs)
                if not args:
                    return
                message = bstack1l1_opy_ (u"ࠩࠣࠫᐩ").join(str(arg) for arg in args)
                if not message.strip():
                    return
                if bstack1l1_opy_ (u"ࠥࡉࡻ࡫࡮ࡵࡆ࡬ࡷࡵࡧࡴࡤࡪࡨࡶࡒࡵࡤࡶ࡮ࡨࠦᐪ") in message:
                    return
                bstack1l11ll11111_opy_ = TestFramework.bstack1l11l11llll_opy_()
                if not bstack1l11ll11111_opy_:
                    return
                bstack1ll111lllll_opy_ = next(
                    (
                        instance
                        for instance in bstack1l11ll11111_opy_
                        if TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1llll111ll1_opy_)
                    ),
                    None,
                )
                if not bstack1ll111lllll_opy_:
                    return
                entry = bstack1ll111ll111_opy_(TestFramework.bstack1ll11111111_opy_, message, bstack1l11lll1111_opy_.bstack1l11l111111_opy_)
                self.bstack1ll1111ll1l_opy_(bstack1ll111lllll_opy_, [entry])
            except Exception as e:
                try:
                    self.bstack1l11l111l11_opy_(bstack1lll1llll11_opy_ (u"ࠦࡠࡋࡶࡦࡰࡷࡈ࡮ࡹࡰࡢࡶࡦ࡬ࡪࡸࡍࡰࡦࡸࡰࡪࡣࠠࡍࡱࡪࠤࡨࡧࡰࡵࡷࡵࡩࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡥࡾࠤᐫ"))
                except:
                    pass
        return bstack1l11l1lllll_opy_
    def bstack1l11l11ll11_opy_(self, event: dict, instance=None) -> None:
        global _1l1llll1lll_opy_
        levels = [bstack1l1_opy_ (u"࡚ࠧࡥࡴࡶࡏࡩࡻ࡫࡬ࠣᐬ"), bstack1l1_opy_ (u"ࠨࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࠥᐭ")]
        bstack1l11l111ll1_opy_ = bstack1l1_opy_ (u"ࠢࠣᐮ")
        if instance is not None:
            try:
                bstack1l11l111ll1_opy_ = TestFramework.get_state(instance, TestFramework.bstack1llll111ll1_opy_)
            except Exception as e:
                self.logger.warning(bstack1l1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡷࡸ࡭ࡩࠦࡦࡳࡱࡰࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࠨᐯ").format(e))
        bstack1l11ll11l11_opy_ = []
        try:
            for level in levels:
                platform_index = os.environ[bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩᐰ")]
                bstack1ll111l1111_opy_ = os.path.join(bstack1ll11lll11l_opy_, (bstack1ll1111llll_opy_ + str(platform_index)), level)
                if not os.path.isdir(bstack1ll111l1111_opy_):
                    self.logger.debug(bstack1l1_opy_ (u"ࠥࡈ࡮ࡸࡥࡤࡶࡲࡶࡾࠦ࡮ࡰࡶࠣࡴࡷ࡫ࡳࡦࡰࡷࠤ࡫ࡵࡲࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫࡚ࠥࡥࡴࡶࠣࡥࡳࡪࠠࡃࡷ࡬ࡰࡩࠦ࡬ࡦࡸࡨࡰࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡿࢂࠨᐱ").format(bstack1ll111l1111_opy_))
                    continue
                file_names = os.listdir(bstack1ll111l1111_opy_)
                for file_name in file_names:
                    file_path = os.path.join(bstack1ll111l1111_opy_, file_name)
                    abs_path = os.path.abspath(file_path)
                    if abs_path in _1l1llll1lll_opy_:
                        self.logger.info(bstack1l1_opy_ (u"ࠦࡕࡧࡴࡩࠢࡤࡰࡷ࡫ࡡࡥࡻࠣࡴࡷࡵࡣࡦࡵࡶࡩࡩࠦࡻࡾࠤᐲ").format(abs_path))
                        continue
                    if os.path.isfile(file_path):
                        try:
                            bstack1l11ll111l1_opy_ = os.path.getmtime(file_path)
                            timestamp = datetime.fromtimestamp(bstack1l11ll111l1_opy_, tz=timezone.utc).isoformat()
                            file_size = os.path.getsize(file_path)
                            if level == bstack1l1_opy_ (u"࡚ࠧࡥࡴࡶࡏࡩࡻ࡫࡬ࠣᐳ"):
                                entry = bstack1ll111ll111_opy_(
                                    kind=bstack1l1_opy_ (u"ࠨࡔࡆࡕࡗࡣࡆ࡚ࡔࡂࡅࡋࡑࡊࡔࡔࠣᐴ"),
                                    message=bstack1l1_opy_ (u"ࠢࠣᐵ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1ll1l1lll11_opy_=file_size,
                                    bstack1ll1l11111l_opy_=bstack1l1_opy_ (u"ࠣࡏࡄࡒ࡚ࡇࡌࡠࡗࡓࡐࡔࡇࡄࠣᐶ"),
                                    bstack11l111l_opy_=os.path.abspath(file_path),
                                    bstack11l1l1llll_opy_=bstack1l11l111ll1_opy_
                                )
                            elif level == bstack1l1_opy_ (u"ࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠨᐷ"):
                                entry = bstack1ll111ll111_opy_(
                                    kind=bstack1l1_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧᐸ"),
                                    message=bstack1l1_opy_ (u"ࠦࠧᐹ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1ll1l1lll11_opy_=file_size,
                                    bstack1ll1l11111l_opy_=bstack1l1_opy_ (u"ࠧࡓࡁࡏࡗࡄࡐࡤ࡛ࡐࡍࡑࡄࡈࠧᐺ"),
                                    bstack11l111l_opy_=os.path.abspath(file_path),
                                    bstack1ll11l1111l_opy_=bstack1l11l111ll1_opy_
                                )
                            bstack1l11ll11l11_opy_.append(entry)
                            _1l1llll1lll_opy_.add(abs_path)
                        except Exception as bstack1l11l1l1lll_opy_:
                            self.logger.error(bstack1l1_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡵࡥ࡮ࡹࡥࡥࠢࡺ࡬ࡪࡴࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴࠢࡾࢁࠧᐻ").format(bstack1l11l1l1lll_opy_))
        except Exception as e:
            self.logger.error(bstack1l1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡶࡦ࡯ࡳࡦࡦࠣࡻ࡭࡫࡮ࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡿࢂࠨᐼ").format(e))
        event[bstack1l1_opy_ (u"ࠣ࡮ࡲ࡫ࡸࠨᐽ")] = bstack1l11ll11l11_opy_
class bstack1l11l11ll1l_opy_(JSONEncoder):
    def __init__(self, **kwargs):
        self.bstack1l11l1ll1ll_opy_ = set()
        kwargs[bstack1l1_opy_ (u"ࠤࡶ࡯࡮ࡶ࡫ࡦࡻࡶࠦᐾ")] = True
        super().__init__(**kwargs)
    def default(self, obj):
        return bstack1l111lll1ll_opy_(obj, self.bstack1l11l1ll1ll_opy_)
def bstack1l11l11l11l_opy_(obj):
    return isinstance(obj, (str, int, float, bool, type(None)))
def bstack1l111lll1ll_opy_(obj, bstack1l11l1ll1ll_opy_=None, max_depth=3):
    if bstack1l11l1ll1ll_opy_ is None:
        bstack1l11l1ll1ll_opy_ = set()
    if id(obj) in bstack1l11l1ll1ll_opy_ or max_depth <= 0:
        return None
    max_depth -= 1
    bstack1l11l1ll1ll_opy_.add(id(obj))
    if isinstance(obj, datetime):
        return obj.isoformat()
    bstack1l11l1lll11_opy_ = TestFramework.bstack1ll1l1l11ll_opy_(obj)
    bstack1l111lllll1_opy_ = next((k.lower() in bstack1l11l1lll11_opy_.lower() for k in bstack1l111llllll_opy_.keys()), None)
    if bstack1l111lllll1_opy_:
        obj = TestFramework.bstack1ll1l1l111l_opy_(obj, bstack1l111llllll_opy_[bstack1l111lllll1_opy_])
    if not isinstance(obj, dict):
        keys = []
        if hasattr(obj, bstack1l1_opy_ (u"ࠥࡣࡤࡹ࡬ࡰࡶࡶࡣࡤࠨᐿ")):
            keys = getattr(obj, bstack1l1_opy_ (u"ࠦࡤࡥࡳ࡭ࡱࡷࡷࡤࡥࠢᑀ"), [])
        elif hasattr(obj, bstack1l1_opy_ (u"ࠧࡥ࡟ࡥ࡫ࡦࡸࡤࡥࠢᑁ")):
            keys = getattr(obj, bstack1l1_opy_ (u"ࠨ࡟ࡠࡦ࡬ࡧࡹࡥ࡟ࠣᑂ"), {}).keys()
        else:
            keys = dir(obj)
        obj = {k: getattr(obj, k, None) for k in keys if not str(k).startswith(bstack1l1_opy_ (u"ࠢࡠࠤᑃ"))}
        if not obj and bstack1l11l1lll11_opy_ == bstack1l1_opy_ (u"ࠣࡲࡤࡸ࡭ࡲࡩࡣ࠰ࡓࡳࡸ࡯ࡸࡑࡣࡷ࡬ࠧᑄ"):
            obj = {bstack1l1_opy_ (u"ࠤࡳࡥࡹ࡮ࠢᑅ"): str(obj)}
    result = {}
    for key, value in obj.items():
        if not bstack1l11l11l11l_opy_(key) or str(key).startswith(bstack1l1_opy_ (u"ࠥࡣࠧᑆ")):
            continue
        if value is not None and bstack1l11l11l11l_opy_(value):
            result[key] = value
        elif isinstance(value, dict):
            r = bstack1l111lll1ll_opy_(value, bstack1l11l1ll1ll_opy_, max_depth)
            if r is not None:
                result[key] = r
        elif isinstance(value, (list, tuple, set, frozenset)):
            result[key] = list(filter(None, [bstack1l111lll1ll_opy_(o, bstack1l11l1ll1ll_opy_, max_depth) for o in value]))
    return result or None