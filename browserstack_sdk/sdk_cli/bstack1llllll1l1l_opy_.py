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
from datetime import datetime
import os
import threading
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import (
    bstack1llll1ll1ll_opy_,
    bstack1lllll1lll1_opy_,
    bstack1lll11ll1l1_opy_,
    bstack1111111l11_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llllll1ll1_opy_ import bstack1lllll1ll11_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_, bstack1lll1l11l11_opy_
from typing import Tuple, Dict, Any, List, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1111111111_opy_ import bstack1llll1ll11l_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l11l1_opy_ import bstack1lll11l111l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1lll1ll_opy_ import bstack1llll1l11ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11l1l_opy_ import bstack1lll1l1ll11_opy_
from bstack_utils.helper import bstack1l1111ll1l1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
from bstack_utils.bstack11l11l1111_opy_ import bstack1lllllllll1_opy_
import grpc
import traceback
import json
class bstack1l1l1llll1l_opy_(bstack1llll1ll11l_opy_):
    bstack1l1ll1l1ll1_opy_ = False
    bstack1l111ll1l1l_opy_ = bstack1lllll1_opy_ (u"ࠦࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠴ࡷࡦࡤࡧࡶ࡮ࡼࡥࡳࠤᐲ")
    bstack1l1111ll111_opy_ = bstack1lllll1_opy_ (u"ࠧࡸࡥ࡮ࡱࡷࡩ࠳ࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲࠣᐳ")
    bstack1l111ll11ll_opy_ = bstack1lllll1_opy_ (u"ࠨࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡩ࡯࡫ࡷࠦᐴ")
    bstack1l1111llll1_opy_ = bstack1lllll1_opy_ (u"ࠢࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡪࡵࡢࡷࡨࡧ࡮࡯࡫ࡱ࡫ࠧᐵ")
    bstack1l111lll11l_opy_ = bstack1lllll1_opy_ (u"ࠣࡦࡵ࡭ࡻ࡫ࡲࡠࡪࡤࡷࡤࡻࡲ࡭ࠤᐶ")
    scripts: Dict[str, Dict[str, str]]
    commands: Dict[str, Dict[str, Dict[str, List[str]]]]
    def __init__(self, bstack1l1l1l111ll_opy_, bstack1ll1lll1ll1_opy_):
        super().__init__()
        self.scripts = dict()
        self.commands = dict()
        self.accessibility = False
        self.bstack1l111ll1ll1_opy_ = False
        self.bstack1l111ll111l_opy_ = dict()
        if not self.is_enabled():
            return
        self.bstack1l11l11l1l1_opy_ = bstack1ll1lll1ll1_opy_
        bstack1l1l1l111ll_opy_.bstack11111111ll_opy_((bstack1llll1ll1ll_opy_.bstack1lllll1l1l1_opy_, bstack1lllll1lll1_opy_.PRE), self.bstack1l111llll11_opy_)
        TestFramework.bstack11111111ll_opy_((bstack1llll11l1ll_opy_.TEST, bstack1llll1l11l1_opy_.PRE), self.bstack1lll1l1lll1_opy_)
        TestFramework.bstack11111111ll_opy_((bstack1llll11l1ll_opy_.TEST, bstack1llll1l11l1_opy_.POST), self.bstack1llll111l1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1l1lll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l111llllll_opy_(instance, args)
        test_framework = f.get_state(instance, TestFramework.bstack1lll1ll1l1l_opy_)
        if self.bstack1l111ll1ll1_opy_:
            self.bstack1l111ll111l_opy_[bstack1lllll1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠤᐷ")] = f.get_state(instance, TestFramework.bstack1lll1lllll1_opy_)
        if bstack1lllll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠧᐸ") in instance.bstack1ll11l1l1l1_opy_:
            platform_index = f.get_state(instance, TestFramework.bstack1111111ll1_opy_)
            self.accessibility = self.bstack1l111l1111l_opy_(tags, self.config[bstack1lllll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧᐹ")][platform_index])
        else:
            capabilities = self.bstack1l11l11l1l1_opy_.bstack1llll1l1111_opy_(f, instance, bstack1lllll111ll_opy_, *args, **kwargs)
            if not capabilities:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠢࡩࡳࡺࡴࡤࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᐺ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠨࠢᐻ"))
                return
            self.accessibility = self.bstack1l111l1111l_opy_(tags, capabilities)
        if self.bstack1l11l11l1l1_opy_.pages and self.bstack1l11l11l1l1_opy_.pages.values():
            bstack1l111l1l1l1_opy_ = list(self.bstack1l11l11l1l1_opy_.pages.values())
            if bstack1l111l1l1l1_opy_ and isinstance(bstack1l111l1l1l1_opy_[0], (list, tuple)) and bstack1l111l1l1l1_opy_[0]:
                bstack1l1111lll1l_opy_ = bstack1l111l1l1l1_opy_[0][0]
                if callable(bstack1l1111lll1l_opy_):
                    page = bstack1l1111lll1l_opy_()
                    def bstack11l111111l_opy_():
                        self.get_accessibility_results(page, bstack1lllll1_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦᐼ"))
                    def bstack1l111l11lll_opy_():
                        self.get_accessibility_results_summary(page, bstack1lllll1_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧᐽ"))
                    setattr(page, bstack1lllll1_opy_ (u"ࠤࡪࡩࡹࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡗ࡫ࡳࡶ࡮ࡷࡷࠧᐾ"), bstack11l111111l_opy_)
                    setattr(page, bstack1lllll1_opy_ (u"ࠥ࡫ࡪࡺࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡘࡥࡴࡷ࡯ࡸࡘࡻ࡭࡮ࡣࡵࡽࠧᐿ"), bstack1l111l11lll_opy_)
        self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡸ࡮࡯ࡶ࡮ࡧࠤࡷࡻ࡮ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡸࡤࡰࡺ࡫࠽ࠣᑀ") + str(self.accessibility) + bstack1lllll1_opy_ (u"ࠧࠨᑁ"))
    def bstack1l111llll11_opy_(
        self,
        f: bstack1lllll1ll11_opy_,
        driver: object,
        exec: Tuple[bstack1111111l11_opy_, str],
        bstack1lllll111ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            bstack1l11llll11_opy_ = datetime.now()
            self.bstack1l111l1l111_opy_(f, exec, *args, **kwargs)
            instance, method_name = exec
            instance.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠨࡡ࠲࠳ࡼ࠾࡮ࡴࡩࡵࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡦࡳࡳ࡬ࡩࡨࠤᑂ"), datetime.now() - bstack1l11llll11_opy_)
            if (
                not f.bstack1l1ll1lllll_opy_(method_name)
                or f.bstack1l1lll111ll_opy_(method_name, *args)
                or f.bstack1l1lll1l1ll_opy_(method_name, *args)
            ):
                return
            if not f.get_state(instance, bstack1l1l1llll1l_opy_.bstack1l111ll11ll_opy_, False):
                if not bstack1l1l1llll1l_opy_.bstack1l1ll1l1ll1_opy_:
                    self.logger.warning(bstack1lllll1_opy_ (u"ࠢ࡜ࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢ࡭ࡳࡪࡥࡹ࠿ࠥᑃ") + str(f.platform_index) + bstack1lllll1_opy_ (u"ࠣ࡟ࠣࡥ࠶࠷ࡹࠡࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠠࡩࡣࡹࡩࠥࡴ࡯ࡵࠢࡥࡩࡪࡴࠠࡴࡧࡷࠤ࡫ࡵࡲࠡࡶ࡫࡭ࡸࠦࡳࡦࡵࡶ࡭ࡴࡴࠢᑄ"))
                    bstack1l1l1llll1l_opy_.bstack1l1ll1l1ll1_opy_ = True
                return
            bstack1l111l1llll_opy_ = self.scripts.get(f.framework_name, {})
            if not bstack1l111l1llll_opy_:
                platform_index = f.get_state(instance, bstack1lllll1ll11_opy_.bstack1111111ll1_opy_, 0)
                self.logger.debug(bstack1lllll1_opy_ (u"ࠤࡱࡳࠥࡧ࠱࠲ࡻࠣࡷࡨࡸࡩࡱࡶࡶࠤ࡫ࡵࡲࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢ࡭ࡳࡪࡥࡹ࠿ࡾࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࢁࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࠢᑅ") + str(f.framework_name) + bstack1lllll1_opy_ (u"ࠥࠦᑆ"))
                return
            command_name = f.bstack1l1lll111l1_opy_(*args)
            if not command_name:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥࡩ࡯࡮࡯ࡤࡲࡩࡥ࡮ࡢ࡯ࡨࠤ࡫ࡵࡲࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪ࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃࠠ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࡂࠨᑇ") + str(method_name) + bstack1lllll1_opy_ (u"ࠧࠨᑈ"))
                return
            bstack1l111lllll1_opy_ = f.get_state(instance, bstack1l1l1llll1l_opy_.bstack1l111lll11l_opy_, False)
            if command_name == bstack1lllll1_opy_ (u"ࠨࡧࡦࡶࠥᑉ") and not bstack1l111lllll1_opy_:
                f.bstack1lllll1l11l_opy_(instance, bstack1l1l1llll1l_opy_.bstack1l111lll11l_opy_, True)
                bstack1l111lllll1_opy_ = True
            if not bstack1l111lllll1_opy_ and not self.bstack1l111ll1ll1_opy_:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠢ࡯ࡱ࡙ࠣࡗࡒࠠ࡭ࡱࡤࡨࡪࡪࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࡽࡩ࠲࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࠦࡣࡰ࡯ࡰࡥࡳࡪ࡟࡯ࡣࡰࡩࡂࠨᑊ") + str(command_name) + bstack1lllll1_opy_ (u"ࠣࠤᑋ"))
                return
            scripts_to_run = self.commands.get(f.framework_name, {}).get(method_name, {}).get(command_name, [])
            if not scripts_to_run:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠤࡱࡳࠥࡧ࠱࠲ࡻࠣࡷࡨࡸࡩࡱࡶࡶࠤ࡫ࡵࡲࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪ࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃࠠࡤࡱࡰࡱࡦࡴࡤࡠࡰࡤࡱࡪࡃࠢᑌ") + str(command_name) + bstack1lllll1_opy_ (u"ࠥࠦᑍ"))
                return
            self.logger.info(bstack1lllll1_opy_ (u"ࠦࡷࡻ࡮࡯࡫ࡱ࡫ࠥࢁ࡬ࡦࡰࠫࡷࡨࡸࡩࡱࡶࡶࡣࡹࡵ࡟ࡳࡷࡱ࠭ࢂࠦࡳࡤࡴ࡬ࡴࡹࡹࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࡽࡩ࠲࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࠦࡣࡰ࡯ࡰࡥࡳࡪ࡟࡯ࡣࡰࡩࡂࠨᑎ") + str(command_name) + bstack1lllll1_opy_ (u"ࠧࠨᑏ"))
            scripts = [(s, bstack1l111l1llll_opy_[s]) for s in scripts_to_run if s in bstack1l111l1llll_opy_]
            for script_name, bstack1llll1111l1_opy_ in scripts:
                try:
                    bstack1l11llll11_opy_ = datetime.now()
                    if script_name == bstack1lllll1_opy_ (u"ࠨࡳࡤࡣࡱࠦᑐ"):
                        result = self.perform_scan(driver, method=command_name, framework_name=f.framework_name)
                    instance.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠢࡢ࠳࠴ࡽ࠿ࠨᑑ") + script_name, datetime.now() - bstack1l11llll11_opy_)
                    if isinstance(result, dict) and not result.get(bstack1lllll1_opy_ (u"ࠣࡵࡸࡧࡨ࡫ࡳࡴࠤᑒ"), True):
                        self.logger.warning(bstack1lllll1_opy_ (u"ࠤࡶ࡯࡮ࡶࠠࡦࡺࡨࡧࡺࡺࡩ࡯ࡩࠣࡶࡪࡳࡡࡪࡰ࡬ࡲ࡬ࠦࡳࡤࡴ࡬ࡴࡹࡹ࠺ࠡࠤᑓ") + str(result) + bstack1lllll1_opy_ (u"ࠥࠦᑔ"))
                        break
                except Exception as e:
                    self.logger.error(bstack1lllll1_opy_ (u"ࠦࡪࡸࡲࡰࡴࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡲ࡬ࠦࡳࡤࡴ࡬ࡴࡹࡃࡻࡴࡥࡵ࡭ࡵࡺ࡟࡯ࡣࡰࡩࢂࠦࡥࡳࡴࡲࡶࡂࠨᑕ") + str(e) + bstack1lllll1_opy_ (u"ࠧࠨᑖ"))
        except Exception as e:
            self.logger.error(bstack1lllll1_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡨࡼࡪࡩࡵࡵࡧࠣࡩࡷࡸ࡯ࡳ࠿ࠥᑗ") + str(e) + bstack1lllll1_opy_ (u"ࠢࠣᑘ"))
    def bstack1llll111l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l111llllll_opy_(instance, args)
        capabilities = self.bstack1l11l11l1l1_opy_.bstack1llll1l1111_opy_(f, instance, bstack1lllll111ll_opy_, *args, **kwargs)
        self.accessibility = self.bstack1l111l1111l_opy_(tags, capabilities)
        if not self.accessibility:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡤ࠵࠶ࡿࠠ࡯ࡱࡷࠤࡪࡴࡡࡣ࡮ࡨࡨࠧᑙ"))
            return
        driver = self.bstack1l11l11l1l1_opy_.bstack1llll11lll1_opy_(f, instance, bstack1lllll111ll_opy_, *args, **kwargs)
        test_name = f.get_state(instance, TestFramework.bstack1ll11l111ll_opy_)
        if not test_name:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡱ࡮ࡹࡳࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡱࡥࡲ࡫ࠢᑚ"))
            return
        test_uuid = f.get_state(instance, TestFramework.bstack1lll1lllll1_opy_)
        if not test_uuid:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡹࡺ࡯ࡤࠣᑛ"))
            return
        if isinstance(self.bstack1l11l11l1l1_opy_, bstack1llll1l11ll_opy_):
            framework_name = bstack1lllll1_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᑜ")
        else:
            framework_name = bstack1lllll1_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧᑝ")
        self.bstack1111l1ll_opy_(driver, test_name, framework_name, test_uuid)
    def perform_scan(self, driver: object, method: Union[None, str], framework_name: str):
        bstack1ll1l1l1111_opy_ = bstack1lllllllll1_opy_.bstack1ll11111ll1_opy_(EVENTS.bstack1l1l1l1ll_opy_.value)
        if not self.accessibility:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠨࡰࡦࡴࡩࡳࡷࡳ࡟ࡴࡥࡤࡲ࠿ࠦࡡ࠲࠳ࡼࠤࡳࡵࡴࠡࡧࡱࡥࡧࡲࡥࡥࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࡿ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࠦࠢᑞ"))
            return
        bstack1l11llll11_opy_ = datetime.now()
        bstack1llll1111l1_opy_ = self.scripts.get(framework_name, {}).get(bstack1lllll1_opy_ (u"ࠢࡴࡥࡤࡲࠧᑟ"), None)
        if not bstack1llll1111l1_opy_:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠣࡲࡨࡶ࡫ࡵࡲ࡮ࡡࡶࡧࡦࡴ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࠪࡷࡨࡧ࡮ࠨࠢࡶࡧࡷ࡯ࡰࡵࠢࡩࡳࡷࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࠣᑠ") + str(framework_name) + bstack1lllll1_opy_ (u"ࠤࠣࠦᑡ"))
            return
        if self.bstack1l111ll1ll1_opy_:
            arg = dict()
            arg[bstack1lllll1_opy_ (u"ࠥࡱࡪࡺࡨࡰࡦࠥᑢ")] = method if method else bstack1lllll1_opy_ (u"ࠦࠧᑣ")
            arg[bstack1lllll1_opy_ (u"ࠧࡺࡨࡕࡧࡶࡸࡗࡻ࡮ࡖࡷ࡬ࡨࠧᑤ")] = self.bstack1l111ll111l_opy_[bstack1lllll1_opy_ (u"ࠨࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩࠨᑥ")]
            arg[bstack1lllll1_opy_ (u"ࠢࡵࡪࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠧᑦ")] = self.bstack1l111ll111l_opy_[bstack1lllll1_opy_ (u"ࠣࡶࡨࡷࡹ࡮ࡵࡣࡡࡥࡹ࡮ࡲࡤࡠࡷࡸ࡭ࡩࠨᑧ")]
            arg[bstack1lllll1_opy_ (u"ࠤࡤࡹࡹ࡮ࡈࡦࡣࡧࡩࡷࠨᑨ")] = self.bstack1l111ll111l_opy_[bstack1lllll1_opy_ (u"ࠥࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡗࡳࡰ࡫࡮ࠣᑩ")]
            arg[bstack1lllll1_opy_ (u"ࠦࡹ࡮ࡊࡸࡶࡗࡳࡰ࡫࡮ࠣᑪ")] = self.bstack1l111ll111l_opy_[bstack1lllll1_opy_ (u"ࠧࡺࡨࡠ࡬ࡺࡸࡤࡺ࡯࡬ࡧࡱࠦᑫ")]
            arg[bstack1lllll1_opy_ (u"ࠨࡳࡤࡣࡱࡘ࡮ࡳࡥࡴࡶࡤࡱࡵࠨᑬ")] = str(int(datetime.now().timestamp() * 1000))
            bstack1l111l11111_opy_ = bstack1llll1111l1_opy_ % json.dumps(arg)
            driver.execute_script(bstack1l111l11111_opy_)
            return
        instance = bstack1lll11ll1l1_opy_.bstack1ll11lll11l_opy_(driver)
        if instance:
            if not bstack1lll11ll1l1_opy_.get_state(instance, bstack1l1l1llll1l_opy_.bstack1l1111llll1_opy_, False):
                bstack1lll11ll1l1_opy_.bstack1lllll1l11l_opy_(instance, bstack1l1l1llll1l_opy_.bstack1l1111llll1_opy_, True)
            else:
                self.logger.info(bstack1lllll1_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࡀࠠࡢ࡮ࡵࡩࡦࡪࡹࠡ࡫ࡱࠤࡵࡸ࡯ࡨࡴࡨࡷࡸࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࡼࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࡱࡪࡺࡨࡰࡦࡀࠦᑭ") + str(method) + bstack1lllll1_opy_ (u"ࠣࠤᑮ"))
                return
        self.logger.info(bstack1lllll1_opy_ (u"ࠤࡳࡩࡷ࡬࡯ࡳ࡯ࡢࡷࡨࡧ࡮࠻ࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࡿ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࠦ࡭ࡦࡶ࡫ࡳࡩࡃࠢᑯ") + str(method) + bstack1lllll1_opy_ (u"ࠥࠦᑰ"))
        if framework_name == bstack1lllll1_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᑱ"):
            result = self.bstack1l11l11l1l1_opy_.bstack1llll1l111l_opy_(driver, bstack1llll1111l1_opy_)
        else:
            result = driver.execute_async_script(bstack1llll1111l1_opy_, {bstack1lllll1_opy_ (u"ࠧࡳࡥࡵࡪࡲࡨࠧᑲ"): method if method else bstack1lllll1_opy_ (u"ࠨࠢᑳ")})
        bstack1lllllllll1_opy_.end(EVENTS.bstack1l1l1l1ll_opy_.value, bstack1ll1l1l1111_opy_+bstack1lllll1_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᑴ"), bstack1ll1l1l1111_opy_+bstack1lllll1_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᑵ"), True, None, command=method)
        if instance:
            bstack1lll11ll1l1_opy_.bstack1lllll1l11l_opy_(instance, bstack1l1l1llll1l_opy_.bstack1l1111llll1_opy_, False)
            instance.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠤࡤ࠵࠶ࡿ࠺ࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࠨᑶ"), datetime.now() - bstack1l11llll11_opy_)
        return result
        def bstack1l111l11l11_opy_(self, driver: object, framework_name, bstack11l1lllll_opy_: str):
            self.bstack1llll1lllll_opy_()
            req = structs.AccessibilityResultRequest()
            req.bin_session_id = self.bin_session_id
            req.bstack1l111l111l1_opy_ = self.bstack1l111ll111l_opy_[bstack1lllll1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠥᑷ")]
            req.bstack11l1lllll_opy_ = bstack11l1lllll_opy_
            req.session_id = self.bin_session_id
            try:
                r = self.bstack1111111l1l_opy_.AccessibilityResult(req)
                if not r.success:
                    self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨᑸ") + str(r) + bstack1lllll1_opy_ (u"ࠧࠨᑹ"))
                else:
                    bstack1l111l11ll1_opy_ = json.loads(r.bstack1l111llll1l_opy_.decode(bstack1lllll1_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᑺ")))
                    if bstack11l1lllll_opy_ == bstack1lllll1_opy_ (u"ࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠫᑻ"):
                        return bstack1l111l11ll1_opy_.get(bstack1lllll1_opy_ (u"ࠣࡦࡤࡸࡦࠨᑼ"), [])
                    else:
                        return bstack1l111l11ll1_opy_.get(bstack1lllll1_opy_ (u"ࠤࡧࡥࡹࡧࠢᑽ"), {})
            except grpc.RpcError as e:
                self.logger.error(bstack1lllll1_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥ࡬ࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡨࡧࡷࡣࡦࡶࡰࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡴࡨࡷࡺࡲࡴࠡࡨࡵࡳࡲࠦࡣ࡭࡫࠽ࠤࠧᑾ") + str(e) + bstack1lllll1_opy_ (u"ࠦࠧᑿ"))
    @measure(event_name=EVENTS.bstack11111lll11_opy_, stage=STAGE.bstack11l1l111l1_opy_)
    def get_accessibility_results(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡵࡩࡸࡻ࡬ࡵࡵ࠽ࠤࡦ࠷࠱ࡺࠢࡱࡳࡹࠦࡥ࡯ࡣࡥࡰࡪࡪࠢᒀ"))
            return
        if self.bstack1l111ll1ll1_opy_:
            self.logger.debug(bstack1lllll1_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡨࡲࡶࠥࡧࡰࡱࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᒁ"))
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l111l11l11_opy_(driver, framework_name, bstack1lllll1_opy_ (u"ࠢࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠦᒂ"))
        bstack1llll1111l1_opy_ = self.scripts.get(framework_name, {}).get(bstack1lllll1_opy_ (u"ࠣࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࠧᒃ"), None)
        if not bstack1llll1111l1_opy_:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠤࡰ࡭ࡸࡹࡩ࡯ࡩࠣࠫ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࠨࠢࡶࡧࡷ࡯ࡰࡵࠢࡩࡳࡷࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࠣᒄ") + str(framework_name) + bstack1lllll1_opy_ (u"ࠥࠦᒅ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1l11llll11_opy_ = datetime.now()
        if framework_name == bstack1lllll1_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᒆ"):
            result = self.bstack1l11l11l1l1_opy_.bstack1llll1l111l_opy_(driver, bstack1llll1111l1_opy_)
        else:
            result = driver.execute_async_script(bstack1llll1111l1_opy_)
        instance = bstack1lll11ll1l1_opy_.bstack1ll11lll11l_opy_(driver)
        if instance:
            instance.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠧࡧ࠱࠲ࡻ࠽࡫ࡪࡺ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡳࡧࡶࡹࡱࡺࡳࠣᒇ"), datetime.now() - bstack1l11llll11_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l111l111l_opy_, stage=STAGE.bstack11l1l111l1_opy_)
    def get_accessibility_results_summary(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠨࡧࡦࡶࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡶࡪࡹࡵ࡭ࡶࡶࡣࡸࡻ࡭࡮ࡣࡵࡽ࠿ࠦࡡ࠲࠳ࡼࠤࡳࡵࡴࠡࡧࡱࡥࡧࡲࡥࡥࠤᒈ"))
            return
        if self.bstack1l111ll1ll1_opy_:
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l111l11l11_opy_(driver, framework_name, bstack1lllll1_opy_ (u"ࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࡗࡺࡳ࡭ࡢࡴࡼࠫᒉ"))
        bstack1llll1111l1_opy_ = self.scripts.get(framework_name, {}).get(bstack1lllll1_opy_ (u"ࠣࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࡘࡻ࡭࡮ࡣࡵࡽࠧᒊ"), None)
        if not bstack1llll1111l1_opy_:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠤࡰ࡭ࡸࡹࡩ࡯ࡩࠣࠫ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࡔࡷࡰࡱࡦࡸࡹࠨࠢࡶࡧࡷ࡯ࡰࡵࠢࡩࡳࡷࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࠣᒋ") + str(framework_name) + bstack1lllll1_opy_ (u"ࠥࠦᒌ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1l11llll11_opy_ = datetime.now()
        if framework_name == bstack1lllll1_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᒍ"):
            result = self.bstack1l11l11l1l1_opy_.bstack1llll1l111l_opy_(driver, bstack1llll1111l1_opy_)
        else:
            result = driver.execute_async_script(bstack1llll1111l1_opy_)
        instance = bstack1lll11ll1l1_opy_.bstack1ll11lll11l_opy_(driver)
        if instance:
            instance.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠧࡧ࠱࠲ࡻ࠽࡫ࡪࡺ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡳࡧࡶࡹࡱࡺࡳࡠࡵࡸࡱࡲࡧࡲࡺࠤᒎ"), datetime.now() - bstack1l11llll11_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l1111ll1ll_opy_, stage=STAGE.bstack11l1l111l1_opy_)
    def bstack1l111ll1111_opy_(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str,
    ):
        self.bstack1llll1lllll_opy_()
        req = structs.AccessibilityConfigRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        try:
            r = self.bstack1111111l1l_opy_.AccessibilityConfig(req)
            if not r.success:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣᒏ") + str(r) + bstack1lllll1_opy_ (u"ࠢࠣᒐ"))
            else:
                self.bstack1l111l11l1l_opy_(framework_name, r)
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1lllll1_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨᒑ") + str(e) + bstack1lllll1_opy_ (u"ࠤࠥᒒ"))
            traceback.print_exc()
            raise e
    def bstack1l111l11l1l_opy_(self, framework_name: str, result: structs.AccessibilityConfigResponse) -> bool:
        if not result.success or not result.accessibility.success:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠥࡰࡴࡧࡤࡠࡥࡲࡲ࡫࡯ࡧ࠻ࠢࡤ࠵࠶ࡿࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦࠥᒓ"))
            return False
        if result.accessibility.is_app_accessibility:
            self.bstack1l111ll1ll1_opy_ = result.accessibility.is_app_accessibility
        if result.testhub.build_hashed_id:
            self.bstack1l111ll111l_opy_[bstack1lllll1_opy_ (u"ࠦࡹ࡫ࡳࡵࡪࡸࡦࡤࡨࡵࡪ࡮ࡧࡣࡺࡻࡩࡥࠤᒔ")] = result.testhub.build_hashed_id
        if result.testhub.jwt:
            self.bstack1l111ll111l_opy_[bstack1lllll1_opy_ (u"ࠧࡺࡨࡠ࡬ࡺࡸࡤࡺ࡯࡬ࡧࡱࠦᒕ")] = result.testhub.jwt
        if result.accessibility.options:
            options = result.accessibility.options
            if options.capabilities:
                for caps in options.capabilities:
                    self.bstack1l111ll111l_opy_[caps.name] = caps.value
            if options.scripts:
                self.scripts[framework_name] = {row.name: row.command for row in options.scripts}
            if options.commands_to_wrap and options.commands_to_wrap.commands:
                scripts_to_run = [s for s in options.commands_to_wrap.scripts_to_run]
                if not scripts_to_run:
                    return False
                bstack1l11l111111_opy_ = dict()
                for command in options.commands_to_wrap.commands:
                    if command.library == self.bstack1l111ll1l1l_opy_ and command.module == self.bstack1l1111ll111_opy_:
                        if command.method and not command.method in bstack1l11l111111_opy_:
                            bstack1l11l111111_opy_[command.method] = dict()
                        if command.name and not command.name in bstack1l11l111111_opy_[command.method]:
                            bstack1l11l111111_opy_[command.method][command.name] = list()
                        bstack1l11l111111_opy_[command.method][command.name].extend(scripts_to_run)
                self.commands[framework_name] = bstack1l11l111111_opy_
        return bool(self.commands.get(framework_name, None))
    def bstack1l111l1l111_opy_(
        self,
        f: bstack1lllll1ll11_opy_,
        exec: Tuple[bstack1111111l11_opy_, str],
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if isinstance(self.bstack1l11l11l1l1_opy_, bstack1llll1l11ll_opy_) and method_name != bstack1lllll1_opy_ (u"࠭ࡣࡰࡰࡱࡩࡨࡺࠧᒖ"):
            return
        if bstack1lll11ll1l1_opy_.bstack1llll1ll1l1_opy_(instance, bstack1l1l1llll1l_opy_.bstack1l111ll11ll_opy_):
            return
        if f.bstack1llllll111l_opy_(method_name, *args):
            bstack1l111ll11l1_opy_ = False
            desired_capabilities = f.bstack1l1lll11l11_opy_(instance)
            if isinstance(desired_capabilities, dict):
                hub_url = f.bstack1l1lll1llll_opy_(instance)
                platform_index = f.get_state(instance, bstack1lllll1ll11_opy_.bstack1111111ll1_opy_, 0)
                bstack1l111ll1lll_opy_ = datetime.now()
                r = self.bstack1l111ll1111_opy_(platform_index, f.framework_name, f.framework_version, hub_url)
                instance.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡩ࡯࡯ࡨ࡬࡫ࠧᒗ"), datetime.now() - bstack1l111ll1lll_opy_)
                bstack1l111ll11l1_opy_ = r.success
            else:
                self.logger.error(bstack1lllll1_opy_ (u"ࠣ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡧࡩࡸ࡯ࡲࡦࡦࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴ࠿ࠥᒘ") + str(desired_capabilities) + bstack1lllll1_opy_ (u"ࠤࠥᒙ"))
            f.bstack1lllll1l11l_opy_(instance, bstack1l1l1llll1l_opy_.bstack1l111ll11ll_opy_, bstack1l111ll11l1_opy_)
    def bstack11l1ll1lll_opy_(self, test_tags):
        bstack1l111ll1111_opy_ = self.config.get(bstack1lllll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᒚ"))
        if not bstack1l111ll1111_opy_:
            return True
        try:
            include_tags = bstack1l111ll1111_opy_[bstack1lllll1_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩᒛ")] if bstack1lllll1_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪᒜ") in bstack1l111ll1111_opy_ and isinstance(bstack1l111ll1111_opy_[bstack1lllll1_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫᒝ")], list) else []
            exclude_tags = bstack1l111ll1111_opy_[bstack1lllll1_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬᒞ")] if bstack1lllll1_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ᒟ") in bstack1l111ll1111_opy_ and isinstance(bstack1l111ll1111_opy_[bstack1lllll1_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧᒠ")], list) else []
            excluded = any(tag in exclude_tags for tag in test_tags)
            included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
            return not excluded and included
        except Exception as error:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡸࡤࡰ࡮ࡪࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡨࡲࡶࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡨࡥࡧࡱࡵࡩࠥࡹࡣࡢࡰࡱ࡭ࡳ࡭࠮ࠡࡇࡵࡶࡴࡸࠠ࠻ࠢࠥᒡ") + str(error))
        return False
    def bstack111lllll1_opy_(self, caps):
        try:
            if self.bstack1l111ll1ll1_opy_:
                bstack1l111l1l1ll_opy_ = caps.get(bstack1lllll1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥᒢ"))
                if bstack1l111l1l1ll_opy_ is not None and str(bstack1l111l1l1ll_opy_).lower() == bstack1lllll1_opy_ (u"ࠧࡧ࡮ࡥࡴࡲ࡭ࡩࠨᒣ"):
                    bstack1l111l1ll11_opy_ = caps.get(bstack1lllll1_opy_ (u"ࠨࡡࡱࡲ࡬ࡹࡲࡀࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣᒤ")) or caps.get(bstack1lllll1_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤᒥ"))
                    if bstack1l111l1ll11_opy_ is not None and int(bstack1l111l1ll11_opy_) < 11:
                        self.logger.warning(bstack1lllll1_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡃࡱࡨࡷࡵࡩࡥࠢ࠴࠵ࠥࡧ࡮ࡥࠢࡤࡦࡴࡼࡥ࠯ࠢࡆࡹࡷࡸࡥ࡯ࡶࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡼࡥࡳࡵ࡬ࡳࡳࠦ࠽ࠣᒦ") + str(bstack1l111l1ll11_opy_) + bstack1lllll1_opy_ (u"ࠤࠥᒧ"))
                        return False
                return True
            bstack1l111lll1l1_opy_ = caps.get(bstack1lllll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᒨ"), {}).get(bstack1lllll1_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨᒩ"), caps.get(bstack1lllll1_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬᒪ"), bstack1lllll1_opy_ (u"࠭ࠧᒫ")))
            if bstack1l111lll1l1_opy_:
                self.logger.warning(bstack1lllll1_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡅࡧࡶ࡯ࡹࡵࡰࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱ࠦᒬ"))
                return False
            browser = caps.get(bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ᒭ"), bstack1lllll1_opy_ (u"ࠩࠪᒮ")).lower()
            if browser != bstack1lllll1_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪᒯ"):
                self.logger.warning(bstack1lllll1_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡈ࡮ࡲࡰ࡯ࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࡸ࠴ࠢᒰ"))
                return False
            bstack1l111lll111_opy_ = bstack1l111l111ll_opy_
            if not self.config.get(bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᒱ")) or self.config.get(bstack1lllll1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪᒲ")):
                bstack1l111lll111_opy_ = bstack1l111l1l11l_opy_
            browser_version = caps.get(bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᒳ"))
            if not browser_version:
                browser_version = caps.get(bstack1lllll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᒴ"), {}).get(bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᒵ"), bstack1lllll1_opy_ (u"ࠪࠫᒶ"))
            if browser_version and browser_version != bstack1lllll1_opy_ (u"ࠫࡱࡧࡴࡦࡵࡷࠫᒷ") and int(browser_version.split(bstack1lllll1_opy_ (u"ࠬ࠴ࠧᒸ"))[0]) <= bstack1l111lll111_opy_:
                self.logger.warning(bstack1lllll1_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡃࡩࡴࡲࡱࡪࠦࡢࡳࡱࡺࡷࡪࡸࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡩࡵࡩࡦࡺࡥࡳࠢࡷ࡬ࡦࡴࠠࠣᒹ") + str(bstack1l111lll111_opy_) + bstack1lllll1_opy_ (u"ࠢ࠯ࠤᒺ"))
                return False
            bstack1l111l1ll1l_opy_ = caps.get(bstack1lllll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᒻ"), {}).get(bstack1lllll1_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᒼ"))
            if not bstack1l111l1ll1l_opy_:
                bstack1l111l1ll1l_opy_ = caps.get(bstack1lllll1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᒽ"), {})
            if bstack1l111l1ll1l_opy_ and bstack1lllll1_opy_ (u"ࠫ࠲࠳ࡨࡦࡣࡧࡰࡪࡹࡳࠨᒾ") in bstack1l111l1ll1l_opy_.get(bstack1lllll1_opy_ (u"ࠬࡧࡲࡨࡵࠪᒿ"), []):
                self.logger.warning(bstack1lllll1_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡰࡲࡸࠥࡸࡵ࡯ࠢࡲࡲࠥࡲࡥࡨࡣࡦࡽࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩ࠳ࠦࡓࡸ࡫ࡷࡧ࡭ࠦࡴࡰࠢࡱࡩࡼࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪࠦ࡯ࡳࠢࡤࡺࡴ࡯ࡤࠡࡷࡶ࡭ࡳ࡭ࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫࠮ࠣᓀ"))
                return False
            return True
        except Exception as error:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡶࡢ࡮࡬ࡨࡦࡺࡥࠡࡣ࠴࠵ࡾࠦࡳࡶࡲࡳࡳࡷࡺࠠ࠻ࠤᓁ") + str(error))
            return False
    def bstack1l1111lllll_opy_(self, test_uuid: str, result: structs.FetchDriverExecuteParamsEventResponse):
        bstack1l111ll1l11_opy_ = {
            bstack1lllll1_opy_ (u"ࠨࡶ࡫ࡘࡪࡹࡴࡓࡷࡱ࡙ࡺ࡯ࡤࠨᓂ"): test_uuid,
        }
        bstack1l1111lll11_opy_ = {}
        if result.success:
            bstack1l1111lll11_opy_ = json.loads(result.accessibility_execute_params)
        return bstack1l1111ll1l1_opy_(bstack1l111ll1l11_opy_, bstack1l1111lll11_opy_)
    def bstack1111l1ll_opy_(self, driver: object, name: str, framework_name: str, test_uuid: str):
        bstack1ll1l1l1111_opy_ = None
        try:
            self.bstack1llll1lllll_opy_()
            req = structs.FetchDriverExecuteParamsEventRequest()
            req.bin_session_id = self.bin_session_id
            req.product = bstack1lllll1_opy_ (u"ࠤࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠤᓃ")
            req.script_name = bstack1lllll1_opy_ (u"ࠥࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠣᓄ")
            r = self.bstack1111111l1l_opy_.FetchDriverExecuteParamsEvent(req)
            if not r.success:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡤࡳ࡫ࡹࡩࡷࠦࡥࡹࡧࡦࡹࡹ࡫ࠠࡱࡣࡵࡥࡲࡹࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢᓅ") + str(r.error) + bstack1lllll1_opy_ (u"ࠧࠨᓆ"))
            else:
                bstack1l111ll1l11_opy_ = self.bstack1l1111lllll_opy_(test_uuid, r)
                bstack1llll1111l1_opy_ = r.script
            self.logger.debug(bstack1lllll1_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡵࡤࡺ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠩᓇ") + str(bstack1l111ll1l11_opy_))
            self.perform_scan(driver, name, framework_name=framework_name)
            if not bstack1llll1111l1_opy_:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࠩࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠧࠡࡵࡦࡶ࡮ࡶࡴࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࠢᓈ") + str(framework_name) + bstack1lllll1_opy_ (u"ࠣࠢࠥᓉ"))
                return
            bstack1ll1l1l1111_opy_ = bstack1lllllllll1_opy_.bstack1ll11111ll1_opy_(EVENTS.bstack1l111lll1ll_opy_.value)
            self.bstack1l111l1lll1_opy_(driver, bstack1llll1111l1_opy_, bstack1l111ll1l11_opy_, framework_name)
            self.logger.info(bstack1lllll1_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣࡪࡴࡸࠠࡵࡪ࡬ࡷࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠧᓊ"))
            bstack1lllllllll1_opy_.end(EVENTS.bstack1l111lll1ll_opy_.value, bstack1ll1l1l1111_opy_+bstack1lllll1_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᓋ"), bstack1ll1l1l1111_opy_+bstack1lllll1_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᓌ"), True, None, command=bstack1lllll1_opy_ (u"ࠬࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠪᓍ"),test_name=name)
        except Exception as bstack1l1111ll11l_opy_:
            self.logger.error(bstack1lllll1_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹࠠࡤࡱࡸࡰࡩࠦ࡮ࡰࡶࠣࡦࡪࠦࡰࡳࡱࡦࡩࡸࡹࡥࡥࠢࡩࡳࡷࠦࡴࡩࡧࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࡀࠠࠣᓎ") + bstack1lllll1_opy_ (u"ࠢࡴࡶࡵࠬࡵࡧࡴࡩࠫࠥᓏ") + bstack1lllll1_opy_ (u"ࠣࠢࡈࡶࡷࡵࡲࠡ࠼ࠥᓐ") + str(bstack1l1111ll11l_opy_))
            bstack1lllllllll1_opy_.end(EVENTS.bstack1l111lll1ll_opy_.value, bstack1ll1l1l1111_opy_+bstack1lllll1_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᓑ"), bstack1ll1l1l1111_opy_+bstack1lllll1_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᓒ"), False, bstack1l1111ll11l_opy_, command=bstack1lllll1_opy_ (u"ࠫࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠩᓓ"),test_name=name)
    def bstack1l111l1lll1_opy_(self, driver, bstack1llll1111l1_opy_, bstack1l111ll1l11_opy_, framework_name):
        if framework_name == bstack1lllll1_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᓔ"):
            self.bstack1l11l11l1l1_opy_.bstack1llll1l111l_opy_(driver, bstack1llll1111l1_opy_, bstack1l111ll1l11_opy_)
        else:
            self.logger.debug(driver.execute_async_script(bstack1llll1111l1_opy_, bstack1l111ll1l11_opy_))
    def _1l111llllll_opy_(self, instance: bstack1lll1l11l11_opy_, args: Tuple) -> list:
        bstack1lllll1_opy_ (u"ࠨࠢࠣࡇࡻࡸࡷࡧࡣࡵࠢࡷࡥ࡬ࡹࠠࡣࡣࡶࡩࡩࠦ࡯࡯ࠢࡷ࡬ࡪࠦࡴࡦࡵࡷࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࠮ࠣࠤࠥᓕ")
        if bstack1lllll1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠫᓖ") in instance.bstack1ll11l1l1l1_opy_:
            return args[2].tags if hasattr(args[2], bstack1lllll1_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭ᓗ")) else []
        if hasattr(args[0], bstack1lllll1_opy_ (u"ࠩࡲࡻࡳࡥ࡭ࡢࡴ࡮ࡩࡷࡹࠧᓘ")):
            return [marker.name for marker in args[0].own_markers]
        return []
    def bstack1l111l1111l_opy_(self, tags, capabilities):
        return self.bstack11l1ll1lll_opy_(tags) and self.bstack111lllll1_opy_(capabilities)