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
from datetime import datetime
import os
import threading
from browserstack_sdk.sdk_cli.bstack111111l11l_opy_ import (
    bstack1llll1lll11_opy_,
    bstack1llll1ll111_opy_,
    bstack1lll111ll11_opy_,
    bstack1llllllll1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllllllll1_opy_ import bstack1lllll111l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_, bstack1lll1llll11_opy_
from typing import Tuple, Dict, Any, List, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1l11l1_opy_ import bstack1111111ll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l11l1_opy_ import bstack1lll111l11l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1llll1l_opy_ import bstack1lll1l1l11l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1lll111_opy_ import bstack1lll1l11ll1_opy_
from bstack_utils.helper import bstack1l1111ll111_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
from bstack_utils.bstack11l1l1111l_opy_ import bstack1llll1ll11l_opy_
import grpc
import traceback
import json
class bstack1l1ll11ll11_opy_(bstack1111111ll1_opy_):
    bstack1l1ll11llll_opy_ = False
    bstack1l111l1llll_opy_ = bstack1l1lll1_opy_ (u"ࠨࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࠯ࡹࡨࡦࡩࡸࡩࡷࡧࡵࠦᐭ")
    bstack1l111ll1111_opy_ = bstack1l1lll1_opy_ (u"ࠢࡳࡧࡰࡳࡹ࡫࠮ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴࠥᐮ")
    bstack1l111ll111l_opy_ = bstack1l1lll1_opy_ (u"ࠣࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠ࡫ࡱ࡭ࡹࠨᐯ")
    bstack1l111llll1l_opy_ = bstack1l1lll1_opy_ (u"ࠤࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡ࡬ࡷࡤࡹࡣࡢࡰࡱ࡭ࡳ࡭ࠢᐰ")
    bstack1l111lll11l_opy_ = bstack1l1lll1_opy_ (u"ࠥࡨࡷ࡯ࡶࡦࡴࡢ࡬ࡦࡹ࡟ࡶࡴ࡯ࠦᐱ")
    scripts: Dict[str, Dict[str, str]]
    commands: Dict[str, Dict[str, Dict[str, List[str]]]]
    def __init__(self, bstack1l1l11l1111_opy_, bstack1ll1lll111l_opy_):
        super().__init__()
        self.scripts = dict()
        self.commands = dict()
        self.accessibility = False
        self.bstack1l111l111l1_opy_ = False
        self.bstack1l111lll111_opy_ = dict()
        if not self.is_enabled():
            return
        self.bstack1l11ll111l1_opy_ = bstack1ll1lll111l_opy_
        bstack1l1l11l1111_opy_.bstack1llllll1111_opy_((bstack1llll1lll11_opy_.bstack1llllllllll_opy_, bstack1llll1ll111_opy_.PRE), self.bstack1l111ll1l1l_opy_)
        TestFramework.bstack1llllll1111_opy_((bstack1lll1ll11ll_opy_.TEST, bstack1lll1lll11l_opy_.PRE), self.bstack1lll1l111ll_opy_)
        TestFramework.bstack1llllll1111_opy_((bstack1lll1ll11ll_opy_.TEST, bstack1lll1lll11l_opy_.POST), self.bstack1llll111l1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1l111ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1llll11_opy_,
        bstack1lllll1llll_opy_: Tuple[bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l111l11ll1_opy_(instance, args)
        test_framework = f.get_state(instance, TestFramework.bstack1llll1l111l_opy_)
        if self.bstack1l111l111l1_opy_:
            self.bstack1l111lll111_opy_[bstack1l1lll1_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠦᐲ")] = f.get_state(instance, TestFramework.bstack1llll11lll1_opy_)
        if bstack1l1lll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠩᐳ") in instance.bstack1ll1111l1l1_opy_:
            platform_index = f.get_state(instance, TestFramework.bstack1llll1l1ll1_opy_)
            self.accessibility = self.bstack1l111lll1ll_opy_(tags, self.config[bstack1l1lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩᐴ")][platform_index])
        else:
            capabilities = self.bstack1l11ll111l1_opy_.bstack1llll1111l1_opy_(f, instance, bstack1lllll1llll_opy_, *args, **kwargs)
            if not capabilities:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠤ࡫ࡵࡵ࡯ࡦࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᐵ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠣࠤᐶ"))
                return
            self.accessibility = self.bstack1l111lll1ll_opy_(tags, capabilities)
        if self.bstack1l11ll111l1_opy_.pages and self.bstack1l11ll111l1_opy_.pages.values():
            bstack1l111ll1l11_opy_ = list(self.bstack1l11ll111l1_opy_.pages.values())
            if bstack1l111ll1l11_opy_ and isinstance(bstack1l111ll1l11_opy_[0], (list, tuple)) and bstack1l111ll1l11_opy_[0]:
                bstack1l111ll1lll_opy_ = bstack1l111ll1l11_opy_[0][0]
                if callable(bstack1l111ll1lll_opy_):
                    page = bstack1l111ll1lll_opy_()
                    def bstack1ll1lll11l_opy_():
                        self.get_accessibility_results(page, bstack1l1lll1_opy_ (u"ࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨᐷ"))
                    def bstack1l111l1l11l_opy_():
                        self.get_accessibility_results_summary(page, bstack1l1lll1_opy_ (u"ࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢᐸ"))
                    setattr(page, bstack1l1lll1_opy_ (u"ࠦ࡬࡫ࡴࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡒࡦࡵࡸࡰࡹࡹࠢᐹ"), bstack1ll1lll11l_opy_)
                    setattr(page, bstack1l1lll1_opy_ (u"ࠧ࡭ࡥࡵࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡓࡧࡶࡹࡱࡺࡓࡶ࡯ࡰࡥࡷࡿࠢᐺ"), bstack1l111l1l11l_opy_)
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠨࡳࡩࡱࡸࡰࡩࠦࡲࡶࡰࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡺࡦࡲࡵࡦ࠿ࠥᐻ") + str(self.accessibility) + bstack1l1lll1_opy_ (u"ࠢࠣᐼ"))
    def bstack1l111ll1l1l_opy_(
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
            bstack11ll11ll1_opy_ = datetime.now()
            self.bstack1l1111l1ll1_opy_(f, exec, *args, **kwargs)
            instance, method_name = exec
            instance.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠣࡣ࠴࠵ࡾࡀࡩ࡯࡫ࡷࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡨࡵ࡮ࡧ࡫ࡪࠦᐽ"), datetime.now() - bstack11ll11ll1_opy_)
            if (
                not f.bstack1l1lll1lll1_opy_(method_name)
                or f.bstack1l1lll1l11l_opy_(method_name, *args)
                or f.bstack1l1lll1llll_opy_(method_name, *args)
            ):
                return
            if not f.get_state(instance, bstack1l1ll11ll11_opy_.bstack1l111ll111l_opy_, False):
                if not bstack1l1ll11ll11_opy_.bstack1l1ll11llll_opy_:
                    self.logger.warning(bstack1l1lll1_opy_ (u"ࠤ࡞ࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࡁࠧᐾ") + str(f.platform_index) + bstack1l1lll1_opy_ (u"ࠥࡡࠥࡧ࠱࠲ࡻࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠢ࡫ࡥࡻ࡫ࠠ࡯ࡱࡷࠤࡧ࡫ࡥ࡯ࠢࡶࡩࡹࠦࡦࡰࡴࠣࡸ࡭࡯ࡳࠡࡵࡨࡷࡸ࡯࡯࡯ࠤᐿ"))
                    bstack1l1ll11ll11_opy_.bstack1l1ll11llll_opy_ = True
                return
            bstack1l1111ll11l_opy_ = self.scripts.get(f.framework_name, {})
            if not bstack1l1111ll11l_opy_:
                platform_index = f.get_state(instance, bstack1lllll111l1_opy_.bstack1llll1l1ll1_opy_, 0)
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡳࡵࠠࡢ࠳࠴ࡽࠥࡹࡣࡳ࡫ࡳࡸࡸࠦࡦࡰࡴࠣࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࡁࢀࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࢃࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࠤᑀ") + str(f.framework_name) + bstack1l1lll1_opy_ (u"ࠧࠨᑁ"))
                return
            command_name = f.bstack1l1llll11l1_opy_(*args)
            if not command_name:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠨ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࡤࡱࡰࡱࡦࡴࡤࡠࡰࡤࡱࡪࠦࡦࡰࡴࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࢀ࡬࠮ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࡾࠢࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫࠽ࠣᑂ") + str(method_name) + bstack1l1lll1_opy_ (u"ࠢࠣᑃ"))
                return
            bstack1l1111llll1_opy_ = f.get_state(instance, bstack1l1ll11ll11_opy_.bstack1l111lll11l_opy_, False)
            if command_name == bstack1l1lll1_opy_ (u"ࠣࡩࡨࡸࠧᑄ") and not bstack1l1111llll1_opy_:
                f.bstack1llll1lllll_opy_(instance, bstack1l1ll11ll11_opy_.bstack1l111lll11l_opy_, True)
                bstack1l1111llll1_opy_ = True
            if not bstack1l1111llll1_opy_ and not self.bstack1l111l111l1_opy_:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠤࡱࡳ࡛ࠥࡒࡍࠢ࡯ࡳࡦࡪࡥࡥࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࡿ࡫࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽࠡࡥࡲࡱࡲࡧ࡮ࡥࡡࡱࡥࡲ࡫࠽ࠣᑅ") + str(command_name) + bstack1l1lll1_opy_ (u"ࠥࠦᑆ"))
                return
            scripts_to_run = self.commands.get(f.framework_name, {}).get(method_name, {}).get(command_name, [])
            if not scripts_to_run:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡳࡵࠠࡢ࠳࠴ࡽࠥࡹࡣࡳ࡫ࡳࡸࡸࠦࡦࡰࡴࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࢀ࡬࠮ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࡾࠢࡦࡳࡲࡳࡡ࡯ࡦࡢࡲࡦࡳࡥ࠾ࠤᑇ") + str(command_name) + bstack1l1lll1_opy_ (u"ࠧࠨᑈ"))
                return
            self.logger.info(bstack1l1lll1_opy_ (u"ࠨࡲࡶࡰࡱ࡭ࡳ࡭ࠠࡼ࡮ࡨࡲ࠭ࡹࡣࡳ࡫ࡳࡸࡸࡥࡴࡰࡡࡵࡹࡳ࠯ࡽࠡࡵࡦࡶ࡮ࡶࡴࡴࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࡿ࡫࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽࠡࡥࡲࡱࡲࡧ࡮ࡥࡡࡱࡥࡲ࡫࠽ࠣᑉ") + str(command_name) + bstack1l1lll1_opy_ (u"ࠢࠣᑊ"))
            scripts = [(s, bstack1l1111ll11l_opy_[s]) for s in scripts_to_run if s in bstack1l1111ll11l_opy_]
            for script_name, bstack1llll11l111_opy_ in scripts:
                try:
                    bstack11ll11ll1_opy_ = datetime.now()
                    if script_name == bstack1l1lll1_opy_ (u"ࠣࡵࡦࡥࡳࠨᑋ"):
                        result = self.perform_scan(driver, method=command_name, framework_name=f.framework_name)
                    instance.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠤࡤ࠵࠶ࡿ࠺ࠣᑌ") + script_name, datetime.now() - bstack11ll11ll1_opy_)
                    if isinstance(result, dict) and not result.get(bstack1l1lll1_opy_ (u"ࠥࡷࡺࡩࡣࡦࡵࡶࠦᑍ"), True):
                        self.logger.warning(bstack1l1lll1_opy_ (u"ࠦࡸࡱࡩࡱࠢࡨࡼࡪࡩࡵࡵ࡫ࡱ࡫ࠥࡸࡥ࡮ࡣ࡬ࡲ࡮ࡴࡧࠡࡵࡦࡶ࡮ࡶࡴࡴ࠼ࠣࠦᑎ") + str(result) + bstack1l1lll1_opy_ (u"ࠧࠨᑏ"))
                        break
                except Exception as e:
                    self.logger.error(bstack1l1lll1_opy_ (u"ࠨࡥࡳࡴࡲࡶࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡴࡧࠡࡵࡦࡶ࡮ࡶࡴ࠾ࡽࡶࡧࡷ࡯ࡰࡵࡡࡱࡥࡲ࡫ࡽࠡࡧࡵࡶࡴࡸ࠽ࠣᑐ") + str(e) + bstack1l1lll1_opy_ (u"ࠢࠣᑑ"))
        except Exception as e:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡪࡾࡥࡤࡷࡷࡩࠥ࡫ࡲࡳࡱࡵࡁࠧᑒ") + str(e) + bstack1l1lll1_opy_ (u"ࠤࠥᑓ"))
    def bstack1llll111l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1llll11_opy_,
        bstack1lllll1llll_opy_: Tuple[bstack1lll1ll11ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l111l11ll1_opy_(instance, args)
        capabilities = self.bstack1l11ll111l1_opy_.bstack1llll1111l1_opy_(f, instance, bstack1lllll1llll_opy_, *args, **kwargs)
        self.accessibility = self.bstack1l111lll1ll_opy_(tags, capabilities)
        if not self.accessibility:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡦ࠷࠱ࡺࠢࡱࡳࡹࠦࡥ࡯ࡣࡥࡰࡪࡪࠢᑔ"))
            return
        driver = self.bstack1l11ll111l1_opy_.bstack1llll111lll_opy_(f, instance, bstack1lllll1llll_opy_, *args, **kwargs)
        test_name = f.get_state(instance, TestFramework.bstack1ll11ll11l1_opy_)
        if not test_name:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡳࡧ࡭ࡦࠤᑕ"))
            return
        test_uuid = f.get_state(instance, TestFramework.bstack1llll11lll1_opy_)
        if not test_uuid:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡻࡵࡪࡦࠥᑖ"))
            return
        if isinstance(self.bstack1l11ll111l1_opy_, bstack1lll1l1l11l_opy_):
            framework_name = bstack1l1lll1_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᑗ")
        else:
            framework_name = bstack1l1lll1_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠩᑘ")
        self.bstack1111lll1_opy_(driver, test_name, framework_name, test_uuid)
    def perform_scan(self, driver: object, method: Union[None, str], framework_name: str):
        bstack1ll1l11l111_opy_ = bstack1llll1ll11l_opy_.bstack1ll1ll1111l_opy_(EVENTS.bstack1l11l1111_opy_.value)
        if not self.accessibility:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡲࡨࡶ࡫ࡵࡲ࡮ࡡࡶࡧࡦࡴ࠺ࠡࡣ࠴࠵ࡾࠦ࡮ࡰࡶࠣࡩࡳࡧࡢ࡭ࡧࡧࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࢁࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽࠡࠤᑙ"))
            return
        bstack11ll11ll1_opy_ = datetime.now()
        bstack1llll11l111_opy_ = self.scripts.get(framework_name, {}).get(bstack1l1lll1_opy_ (u"ࠤࡶࡧࡦࡴࠢᑚ"), None)
        if not bstack1llll11l111_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠥࡴࡪࡸࡦࡰࡴࡰࡣࡸࡩࡡ࡯࠼ࠣࡱ࡮ࡹࡳࡪࡰࡪࠤࠬࡹࡣࡢࡰࠪࠤࡸࡩࡲࡪࡲࡷࠤ࡫ࡵࡲࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࠥᑛ") + str(framework_name) + bstack1l1lll1_opy_ (u"ࠦࠥࠨᑜ"))
            return
        if self.bstack1l111l111l1_opy_:
            arg = dict()
            arg[bstack1l1lll1_opy_ (u"ࠧࡳࡥࡵࡪࡲࡨࠧᑝ")] = method if method else bstack1l1lll1_opy_ (u"ࠨࠢᑞ")
            arg[bstack1l1lll1_opy_ (u"ࠢࡵࡪࡗࡩࡸࡺࡒࡶࡰࡘࡹ࡮ࡪࠢᑟ")] = self.bstack1l111lll111_opy_[bstack1l1lll1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠣᑠ")]
            arg[bstack1l1lll1_opy_ (u"ࠤࡷ࡬ࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠢᑡ")] = self.bstack1l111lll111_opy_[bstack1l1lll1_opy_ (u"ࠥࡸࡪࡹࡴࡩࡷࡥࡣࡧࡻࡩ࡭ࡦࡢࡹࡺ࡯ࡤࠣᑢ")]
            arg[bstack1l1lll1_opy_ (u"ࠦࡦࡻࡴࡩࡊࡨࡥࡩ࡫ࡲࠣᑣ")] = self.bstack1l111lll111_opy_[bstack1l1lll1_opy_ (u"ࠧࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ࡙ࡵ࡫ࡦࡰࠥᑤ")]
            arg[bstack1l1lll1_opy_ (u"ࠨࡴࡩࡌࡺࡸ࡙ࡵ࡫ࡦࡰࠥᑥ")] = self.bstack1l111lll111_opy_[bstack1l1lll1_opy_ (u"ࠢࡵࡪࡢ࡮ࡼࡺ࡟ࡵࡱ࡮ࡩࡳࠨᑦ")]
            arg[bstack1l1lll1_opy_ (u"ࠣࡵࡦࡥࡳ࡚ࡩ࡮ࡧࡶࡸࡦࡳࡰࠣᑧ")] = str(int(datetime.now().timestamp() * 1000))
            bstack1l1111lll11_opy_ = bstack1llll11l111_opy_ % json.dumps(arg)
            driver.execute_script(bstack1l1111lll11_opy_)
            return
        instance = bstack1lll111ll11_opy_.bstack1ll111lllll_opy_(driver)
        if instance:
            if not bstack1lll111ll11_opy_.get_state(instance, bstack1l1ll11ll11_opy_.bstack1l111llll1l_opy_, False):
                bstack1lll111ll11_opy_.bstack1llll1lllll_opy_(instance, bstack1l1ll11ll11_opy_.bstack1l111llll1l_opy_, True)
            else:
                self.logger.info(bstack1l1lll1_opy_ (u"ࠤࡳࡩࡷ࡬࡯ࡳ࡯ࡢࡷࡨࡧ࡮࠻ࠢࡤࡰࡷ࡫ࡡࡥࡻࠣ࡭ࡳࠦࡰࡳࡱࡪࡶࡪࡹࡳࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁࠥࡳࡥࡵࡪࡲࡨࡂࠨᑨ") + str(method) + bstack1l1lll1_opy_ (u"ࠥࠦᑩ"))
                return
        self.logger.info(bstack1l1lll1_opy_ (u"ࠦࡵ࡫ࡲࡧࡱࡵࡱࡤࡹࡣࡢࡰ࠽ࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࢁࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽࠡ࡯ࡨࡸ࡭ࡵࡤ࠾ࠤᑪ") + str(method) + bstack1l1lll1_opy_ (u"ࠧࠨᑫ"))
        if framework_name == bstack1l1lll1_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᑬ"):
            result = self.bstack1l11ll111l1_opy_.bstack1lll1l1lll1_opy_(driver, bstack1llll11l111_opy_)
        else:
            result = driver.execute_async_script(bstack1llll11l111_opy_, {bstack1l1lll1_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪࠢᑭ"): method if method else bstack1l1lll1_opy_ (u"ࠣࠤᑮ")})
        bstack1llll1ll11l_opy_.end(EVENTS.bstack1l11l1111_opy_.value, bstack1ll1l11l111_opy_+bstack1l1lll1_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᑯ"), bstack1ll1l11l111_opy_+bstack1l1lll1_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᑰ"), True, None, command=method)
        if instance:
            bstack1lll111ll11_opy_.bstack1llll1lllll_opy_(instance, bstack1l1ll11ll11_opy_.bstack1l111llll1l_opy_, False)
            instance.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠦࡦ࠷࠱ࡺ࠼ࡳࡩࡷ࡬࡯ࡳ࡯ࡢࡷࡨࡧ࡮ࠣᑱ"), datetime.now() - bstack11ll11ll1_opy_)
        return result
        def bstack1l111l1111l_opy_(self, driver: object, framework_name, bstack1l11l11lll_opy_: str):
            self.bstack1llll1llll1_opy_()
            req = structs.AccessibilityResultRequest()
            req.bin_session_id = self.bin_session_id
            req.bstack1l1111lll1l_opy_ = self.bstack1l111lll111_opy_[bstack1l1lll1_opy_ (u"ࠧࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠧᑲ")]
            req.bstack1l11l11lll_opy_ = bstack1l11l11lll_opy_
            req.session_id = self.bin_session_id
            try:
                r = self.bstack1lllll1ll11_opy_.AccessibilityResult(req)
                if not r.success:
                    self.logger.debug(bstack1l1lll1_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣᑳ") + str(r) + bstack1l1lll1_opy_ (u"ࠢࠣᑴ"))
                else:
                    bstack1l1111ll1ll_opy_ = json.loads(r.bstack1l111l111ll_opy_.decode(bstack1l1lll1_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᑵ")))
                    if bstack1l11l11lll_opy_ == bstack1l1lll1_opy_ (u"ࠩࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࠭ᑶ"):
                        return bstack1l1111ll1ll_opy_.get(bstack1l1lll1_opy_ (u"ࠥࡨࡦࡺࡡࠣᑷ"), [])
                    else:
                        return bstack1l1111ll1ll_opy_.get(bstack1l1lll1_opy_ (u"ࠦࡩࡧࡴࡢࠤᑸ"), {})
            except grpc.RpcError as e:
                self.logger.error(bstack1l1lll1_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡧࡧࡷࡧ࡭࡯࡮ࡨࠢࡪࡩࡹࡥࡡࡱࡲࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡶࡪࡹࡵ࡭ࡶࠣࡪࡷࡵ࡭ࠡࡥ࡯࡭࠿ࠦࠢᑹ") + str(e) + bstack1l1lll1_opy_ (u"ࠨࠢᑺ"))
    @measure(event_name=EVENTS.bstack1ll1lll111_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def get_accessibility_results(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡨࡧࡷࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡷ࡫ࡳࡶ࡮ࡷࡷ࠿ࠦࡡ࠲࠳ࡼࠤࡳࡵࡴࠡࡧࡱࡥࡧࡲࡥࡥࠤᑻ"))
            return
        if self.bstack1l111l111l1_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡪࡴࡸࠠࡢࡲࡳࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᑼ"))
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l111l1111l_opy_(driver, framework_name, bstack1l1lll1_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸࠨᑽ"))
        bstack1llll11l111_opy_ = self.scripts.get(framework_name, {}).get(bstack1l1lll1_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠢᑾ"), None)
        if not bstack1llll11l111_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࠪࠤࡸࡩࡲࡪࡲࡷࠤ࡫ࡵࡲࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࠥᑿ") + str(framework_name) + bstack1l1lll1_opy_ (u"ࠧࠨᒀ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack11ll11ll1_opy_ = datetime.now()
        if framework_name == bstack1l1lll1_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᒁ"):
            result = self.bstack1l11ll111l1_opy_.bstack1lll1l1lll1_opy_(driver, bstack1llll11l111_opy_)
        else:
            result = driver.execute_async_script(bstack1llll11l111_opy_)
        instance = bstack1lll111ll11_opy_.bstack1ll111lllll_opy_(driver)
        if instance:
            instance.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠢࡢ࠳࠴ࡽ࠿࡭ࡥࡵࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡵࡩࡸࡻ࡬ࡵࡵࠥᒂ"), datetime.now() - bstack11ll11ll1_opy_)
        return result
    @measure(event_name=EVENTS.bstack1ll1lllll1_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def get_accessibility_results_summary(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡩࡨࡸࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡸࡥࡴࡷ࡯ࡸࡸࡥࡳࡶ࡯ࡰࡥࡷࡿ࠺ࠡࡣ࠴࠵ࡾࠦ࡮ࡰࡶࠣࡩࡳࡧࡢ࡭ࡧࡧࠦᒃ"))
            return
        if self.bstack1l111l111l1_opy_:
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l111l1111l_opy_(driver, framework_name, bstack1l1lll1_opy_ (u"ࠩࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࡙ࡵ࡮࡯ࡤࡶࡾ࠭ᒄ"))
        bstack1llll11l111_opy_ = self.scripts.get(framework_name, {}).get(bstack1l1lll1_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࡓࡶ࡯ࡰࡥࡷࡿࠢᒅ"), None)
        if not bstack1llll11l111_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࡖࡹࡲࡳࡡࡳࡻࠪࠤࡸࡩࡲࡪࡲࡷࠤ࡫ࡵࡲࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࠥᒆ") + str(framework_name) + bstack1l1lll1_opy_ (u"ࠧࠨᒇ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack11ll11ll1_opy_ = datetime.now()
        if framework_name == bstack1l1lll1_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᒈ"):
            result = self.bstack1l11ll111l1_opy_.bstack1lll1l1lll1_opy_(driver, bstack1llll11l111_opy_)
        else:
            result = driver.execute_async_script(bstack1llll11l111_opy_)
        instance = bstack1lll111ll11_opy_.bstack1ll111lllll_opy_(driver)
        if instance:
            instance.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠢࡢ࠳࠴ࡽ࠿࡭ࡥࡵࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡵࡩࡸࡻ࡬ࡵࡵࡢࡷࡺࡳ࡭ࡢࡴࡼࠦᒉ"), datetime.now() - bstack11ll11ll1_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l111lll1l1_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def bstack1l111l1ll11_opy_(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str,
    ):
        self.bstack1llll1llll1_opy_()
        req = structs.AccessibilityConfigRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        try:
            r = self.bstack1lllll1ll11_opy_.AccessibilityConfig(req)
            if not r.success:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࠥᒊ") + str(r) + bstack1l1lll1_opy_ (u"ࠤࠥᒋ"))
            else:
                self.bstack1l1111ll1l1_opy_(framework_name, r)
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣᒌ") + str(e) + bstack1l1lll1_opy_ (u"ࠦࠧᒍ"))
            traceback.print_exc()
            raise e
    def bstack1l1111ll1l1_opy_(self, framework_name: str, result: structs.AccessibilityConfigResponse) -> bool:
        if not result.success or not result.accessibility.success:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠧࡲ࡯ࡢࡦࡢࡧࡴࡴࡦࡪࡩ࠽ࠤࡦ࠷࠱ࡺࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨࠧᒎ"))
            return False
        if result.accessibility.is_app_accessibility:
            self.bstack1l111l111l1_opy_ = result.accessibility.is_app_accessibility
        if result.testhub.build_hashed_id:
            self.bstack1l111lll111_opy_[bstack1l1lll1_opy_ (u"ࠨࡴࡦࡵࡷ࡬ࡺࡨ࡟ࡣࡷ࡬ࡰࡩࡥࡵࡶ࡫ࡧࠦᒏ")] = result.testhub.build_hashed_id
        if result.testhub.jwt:
            self.bstack1l111lll111_opy_[bstack1l1lll1_opy_ (u"ࠢࡵࡪࡢ࡮ࡼࡺ࡟ࡵࡱ࡮ࡩࡳࠨᒐ")] = result.testhub.jwt
        if result.accessibility.options:
            options = result.accessibility.options
            if options.capabilities:
                for caps in options.capabilities:
                    self.bstack1l111lll111_opy_[caps.name] = caps.value
            if options.scripts:
                self.scripts[framework_name] = {row.name: row.command for row in options.scripts}
            if options.commands_to_wrap and options.commands_to_wrap.commands:
                scripts_to_run = [s for s in options.commands_to_wrap.scripts_to_run]
                if not scripts_to_run:
                    return False
                bstack1l111l11l11_opy_ = dict()
                for command in options.commands_to_wrap.commands:
                    if command.library == self.bstack1l111l1llll_opy_ and command.module == self.bstack1l111ll1111_opy_:
                        if command.method and not command.method in bstack1l111l11l11_opy_:
                            bstack1l111l11l11_opy_[command.method] = dict()
                        if command.name and not command.name in bstack1l111l11l11_opy_[command.method]:
                            bstack1l111l11l11_opy_[command.method][command.name] = list()
                        bstack1l111l11l11_opy_[command.method][command.name].extend(scripts_to_run)
                self.commands[framework_name] = bstack1l111l11l11_opy_
        return bool(self.commands.get(framework_name, None))
    def bstack1l1111l1ll1_opy_(
        self,
        f: bstack1lllll111l1_opy_,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if isinstance(self.bstack1l11ll111l1_opy_, bstack1lll1l1l11l_opy_) and method_name != bstack1l1lll1_opy_ (u"ࠨࡥࡲࡲࡳ࡫ࡣࡵࠩᒑ"):
            return
        if bstack1lll111ll11_opy_.bstack1llllll111l_opy_(instance, bstack1l1ll11ll11_opy_.bstack1l111ll111l_opy_):
            return
        if f.bstack1111111l1l_opy_(method_name, *args):
            bstack1l111l1l1l1_opy_ = False
            desired_capabilities = f.bstack1l1lll1111l_opy_(instance)
            if isinstance(desired_capabilities, dict):
                hub_url = f.bstack1l1lll1l111_opy_(instance)
                platform_index = f.get_state(instance, bstack1lllll111l1_opy_.bstack1llll1l1ll1_opy_, 0)
                bstack1l1111l1l1l_opy_ = datetime.now()
                r = self.bstack1l111l1ll11_opy_(platform_index, f.framework_name, f.framework_version, hub_url)
                instance.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡤࡱࡱࡪ࡮࡭ࠢᒒ"), datetime.now() - bstack1l1111l1l1l_opy_)
                bstack1l111l1l1l1_opy_ = r.success
            else:
                self.logger.error(bstack1l1lll1_opy_ (u"ࠥࡱ࡮ࡹࡳࡪࡰࡪࠤࡩ࡫ࡳࡪࡴࡨࡨࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࡁࠧᒓ") + str(desired_capabilities) + bstack1l1lll1_opy_ (u"ࠦࠧᒔ"))
            f.bstack1llll1lllll_opy_(instance, bstack1l1ll11ll11_opy_.bstack1l111ll111l_opy_, bstack1l111l1l1l1_opy_)
    def bstack1ll11111l1_opy_(self, test_tags):
        bstack1l111l1ll11_opy_ = self.config.get(bstack1l1lll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬᒕ"))
        if not bstack1l111l1ll11_opy_:
            return True
        try:
            include_tags = bstack1l111l1ll11_opy_[bstack1l1lll1_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫᒖ")] if bstack1l1lll1_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬᒗ") in bstack1l111l1ll11_opy_ and isinstance(bstack1l111l1ll11_opy_[bstack1l1lll1_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ᒘ")], list) else []
            exclude_tags = bstack1l111l1ll11_opy_[bstack1l1lll1_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧᒙ")] if bstack1l1lll1_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨᒚ") in bstack1l111l1ll11_opy_ and isinstance(bstack1l111l1ll11_opy_[bstack1l1lll1_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩᒛ")], list) else []
            excluded = any(tag in exclude_tags for tag in test_tags)
            included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
            return not excluded and included
        except Exception as error:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡺࡦࡲࡩࡥࡣࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡪࡴࡸࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡥࡤࡲࡳ࡯࡮ࡨ࠰ࠣࡉࡷࡸ࡯ࡳࠢ࠽ࠤࠧᒜ") + str(error))
        return False
    def bstack1l11ll1l11_opy_(self, caps):
        try:
            if self.bstack1l111l111l1_opy_:
                bstack1l111l11lll_opy_ = caps.get(bstack1l1lll1_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧᒝ"))
                if bstack1l111l11lll_opy_ is not None and str(bstack1l111l11lll_opy_).lower() == bstack1l1lll1_opy_ (u"ࠢࡢࡰࡧࡶࡴ࡯ࡤࠣᒞ"):
                    bstack1l111l1l111_opy_ = caps.get(bstack1l1lll1_opy_ (u"ࠣࡣࡳࡴ࡮ࡻ࡭࠻ࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥᒟ")) or caps.get(bstack1l1lll1_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦᒠ"))
                    if bstack1l111l1l111_opy_ is not None and int(bstack1l111l1l111_opy_) < 11:
                        self.logger.warning(bstack1l1lll1_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡅࡳࡪࡲࡰ࡫ࡧࠤ࠶࠷ࠠࡢࡰࡧࠤࡦࡨ࡯ࡷࡧ࠱ࠤࡈࡻࡲࡳࡧࡱࡸࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡ࠿ࠥᒡ") + str(bstack1l111l1l111_opy_) + bstack1l1lll1_opy_ (u"ࠦࠧᒢ"))
                        return False
                return True
            bstack1l111l1lll1_opy_ = caps.get(bstack1l1lll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᒣ"), {}).get(bstack1l1lll1_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪᒤ"), caps.get(bstack1l1lll1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧᒥ"), bstack1l1lll1_opy_ (u"ࠨࠩᒦ")))
            if bstack1l111l1lll1_opy_:
                self.logger.warning(bstack1l1lll1_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡇࡩࡸࡱࡴࡰࡲࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨᒧ"))
                return False
            browser = caps.get(bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨᒨ"), bstack1l1lll1_opy_ (u"ࠫࠬᒩ")).lower()
            if browser != bstack1l1lll1_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬᒪ"):
                self.logger.warning(bstack1l1lll1_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡃࡩࡴࡲࡱࡪࠦࡢࡳࡱࡺࡷࡪࡸࡳ࠯ࠤᒫ"))
                return False
            bstack1l111ll1ll1_opy_ = bstack1l1111lllll_opy_
            if not self.config.get(bstack1l1lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᒬ")) or self.config.get(bstack1l1lll1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬᒭ")):
                bstack1l111ll1ll1_opy_ = bstack1l111llll11_opy_
            browser_version = caps.get(bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᒮ"))
            if not browser_version:
                browser_version = caps.get(bstack1l1lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᒯ"), {}).get(bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᒰ"), bstack1l1lll1_opy_ (u"ࠬ࠭ᒱ"))
            if browser_version and browser_version != bstack1l1lll1_opy_ (u"࠭࡬ࡢࡶࡨࡷࡹ࠭ᒲ") and int(browser_version.split(bstack1l1lll1_opy_ (u"ࠧ࠯ࠩᒳ"))[0]) <= bstack1l111ll1ll1_opy_:
                self.logger.warning(bstack1l1lll1_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࠢࡹࡩࡷࡹࡩࡰࡰࠣ࡫ࡷ࡫ࡡࡵࡧࡵࠤࡹ࡮ࡡ࡯ࠢࠥᒴ") + str(bstack1l111ll1ll1_opy_) + bstack1l1lll1_opy_ (u"ࠤ࠱ࠦᒵ"))
                return False
            bstack1l111l1ll1l_opy_ = caps.get(bstack1l1lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᒶ"), {}).get(bstack1l1lll1_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫᒷ"))
            if not bstack1l111l1ll1l_opy_:
                bstack1l111l1ll1l_opy_ = caps.get(bstack1l1lll1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪᒸ"), {})
            if bstack1l111l1ll1l_opy_ and bstack1l1lll1_opy_ (u"࠭࠭࠮ࡪࡨࡥࡩࡲࡥࡴࡵࠪᒹ") in bstack1l111l1ll1l_opy_.get(bstack1l1lll1_opy_ (u"ࠧࡢࡴࡪࡷࠬᒺ"), []):
                self.logger.warning(bstack1l1lll1_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡲࡴࡺࠠࡳࡷࡱࠤࡴࡴࠠ࡭ࡧࡪࡥࡨࡿࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫࠮ࠡࡕࡺ࡭ࡹࡩࡨࠡࡶࡲࠤࡳ࡫ࡷࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥࠡࡱࡵࠤࡦࡼ࡯ࡪࡦࠣࡹࡸ࡯࡮ࡨࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠥᒻ"))
                return False
            return True
        except Exception as error:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡸࡤࡰ࡮ࡪࡡࡵࡧࠣࡥ࠶࠷ࡹࠡࡵࡸࡴࡵࡵࡲࡵࠢ࠽ࠦᒼ") + str(error))
            return False
    def bstack1l1111l1lll_opy_(self, test_uuid: str, result: structs.FetchDriverExecuteParamsEventResponse):
        bstack1l111l11111_opy_ = {
            bstack1l1lll1_opy_ (u"ࠪࡸ࡭࡚ࡥࡴࡶࡕࡹࡳ࡛ࡵࡪࡦࠪᒽ"): test_uuid,
        }
        bstack1l111l11l1l_opy_ = {}
        if result.success:
            bstack1l111l11l1l_opy_ = json.loads(result.accessibility_execute_params)
        return bstack1l1111ll111_opy_(bstack1l111l11111_opy_, bstack1l111l11l1l_opy_)
    def bstack1111lll1_opy_(self, driver: object, name: str, framework_name: str, test_uuid: str):
        bstack1ll1l11l111_opy_ = None
        try:
            self.bstack1llll1llll1_opy_()
            req = structs.FetchDriverExecuteParamsEventRequest()
            req.bin_session_id = self.bin_session_id
            req.product = bstack1l1lll1_opy_ (u"ࠦࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠦᒾ")
            req.script_name = bstack1l1lll1_opy_ (u"ࠧࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠥᒿ")
            r = self.bstack1lllll1ll11_opy_.FetchDriverExecuteParamsEvent(req)
            if not r.success:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡦࡵ࡭ࡻ࡫ࡲࠡࡧࡻࡩࡨࡻࡴࡦࠢࡳࡥࡷࡧ࡭ࡴࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࠤᓀ") + str(r.error) + bstack1l1lll1_opy_ (u"ࠢࠣᓁ"))
            else:
                bstack1l111l11111_opy_ = self.bstack1l1111l1lll_opy_(test_uuid, r)
                bstack1llll11l111_opy_ = r.script
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡦࡪ࡬࡯ࡳࡧࠣࡷࡦࡼࡩ࡯ࡩࠣࡶࡪࡹࡵ࡭ࡶࡶࠫᓂ") + str(bstack1l111l11111_opy_))
            self.perform_scan(driver, name, framework_name=framework_name)
            if not bstack1llll11l111_opy_:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠤࡳࡩࡷ࡬࡯ࡳ࡯ࡢࡷࡨࡧ࡮࠻ࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࠫࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠩࠣࡷࡨࡸࡩࡱࡶࠣࡪࡴࡸࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࠤᓃ") + str(framework_name) + bstack1l1lll1_opy_ (u"ࠥࠤࠧᓄ"))
                return
            bstack1ll1l11l111_opy_ = bstack1llll1ll11l_opy_.bstack1ll1ll1111l_opy_(EVENTS.bstack1l111l1l1ll_opy_.value)
            self.bstack1l111ll11l1_opy_(driver, bstack1llll11l111_opy_, bstack1l111l11111_opy_, framework_name)
            self.logger.info(bstack1l1lll1_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡹ࡫ࡳࡵ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡷ࡬࡮ࡹࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣ࡬ࡦࡹࠠࡦࡰࡧࡩࡩ࠴ࠢᓅ"))
            bstack1llll1ll11l_opy_.end(EVENTS.bstack1l111l1l1ll_opy_.value, bstack1ll1l11l111_opy_+bstack1l1lll1_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᓆ"), bstack1ll1l11l111_opy_+bstack1l1lll1_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᓇ"), True, None, command=bstack1l1lll1_opy_ (u"ࠧࡴࡣࡹࡩࡗ࡫ࡳࡶ࡮ࡷࡷࠬᓈ"),test_name=name)
        except Exception as bstack1l111ll11ll_opy_:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴࠢࡦࡳࡺࡲࡤࠡࡰࡲࡸࠥࡨࡥࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡧࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥ࠻ࠢࠥᓉ") + bstack1l1lll1_opy_ (u"ࠤࡶࡸࡷ࠮ࡰࡢࡶ࡫࠭ࠧᓊ") + bstack1l1lll1_opy_ (u"ࠥࠤࡊࡸࡲࡰࡴࠣ࠾ࠧᓋ") + str(bstack1l111ll11ll_opy_))
            bstack1llll1ll11l_opy_.end(EVENTS.bstack1l111l1l1ll_opy_.value, bstack1ll1l11l111_opy_+bstack1l1lll1_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᓌ"), bstack1ll1l11l111_opy_+bstack1l1lll1_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᓍ"), False, bstack1l111ll11ll_opy_, command=bstack1l1lll1_opy_ (u"࠭ࡳࡢࡸࡨࡖࡪࡹࡵ࡭ࡶࡶࠫᓎ"),test_name=name)
    def bstack1l111ll11l1_opy_(self, driver, bstack1llll11l111_opy_, bstack1l111l11111_opy_, framework_name):
        if framework_name == bstack1l1lll1_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫᓏ"):
            self.bstack1l11ll111l1_opy_.bstack1lll1l1lll1_opy_(driver, bstack1llll11l111_opy_, bstack1l111l11111_opy_)
        else:
            self.logger.debug(driver.execute_async_script(bstack1llll11l111_opy_, bstack1l111l11111_opy_))
    def _1l111l11ll1_opy_(self, instance: bstack1lll1llll11_opy_, args: Tuple) -> list:
        bstack1l1lll1_opy_ (u"ࠣࠤࠥࡉࡽࡺࡲࡢࡥࡷࠤࡹࡧࡧࡴࠢࡥࡥࡸ࡫ࡤࠡࡱࡱࠤࡹ࡮ࡥࠡࡶࡨࡷࡹࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬࠰ࠥࠦࠧᓐ")
        if bstack1l1lll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩ࠭ᓑ") in instance.bstack1ll1111l1l1_opy_:
            return args[2].tags if hasattr(args[2], bstack1l1lll1_opy_ (u"ࠪࡸࡦ࡭ࡳࠨᓒ")) else []
        if hasattr(args[0], bstack1l1lll1_opy_ (u"ࠫࡴࡽ࡮ࡠ࡯ࡤࡶࡰ࡫ࡲࡴࠩᓓ")):
            return [marker.name for marker in args[0].own_markers]
        return []
    def bstack1l111lll1ll_opy_(self, tags, capabilities):
        return self.bstack1ll11111l1_opy_(tags) and self.bstack1l11ll1l11_opy_(capabilities)