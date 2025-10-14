# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
from datetime import datetime
import os
import threading
from browserstack_sdk.sdk_cli.bstack1llllll111l_opy_ import (
    bstack1llll1l1lll_opy_,
    bstack1111111l1l_opy_,
    bstack1lll11ll111_opy_,
    bstack1111111111_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1l11ll_opy_ import bstack1llllll11l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_, bstack1lll1l1ll11_opy_
from typing import Tuple, Dict, Any, List, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lllllll111_opy_ import bstack1lllll1l111_opy_
from browserstack_sdk.sdk_cli.bstack1lll111l1ll_opy_ import bstack1lll111lll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1l11_opy_ import bstack1lll1ll11ll_opy_
from browserstack_sdk.sdk_cli.bstack1llll11l1l1_opy_ import bstack1lll1ll11l1_opy_
from bstack_utils.helper import bstack1l1111llll1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
from bstack_utils.bstack1l1l1111ll_opy_ import bstack111111111l_opy_
import grpc
import traceback
import json
class bstack1l1l111111l_opy_(bstack1lllll1l111_opy_):
    bstack1l1ll11llll_opy_ = False
    bstack1l1111ll1l1_opy_ = bstack11l1l11_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱ࠳ࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲࠣᐪ")
    bstack1l111lllll1_opy_ = bstack11l1l11_opy_ (u"ࠦࡷ࡫࡭ࡰࡶࡨ࠲ࡼ࡫ࡢࡥࡴ࡬ࡺࡪࡸࠢᐫ")
    bstack1l111l1l111_opy_ = bstack11l1l11_opy_ (u"ࠧࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤ࡯࡮ࡪࡶࠥᐬ")
    bstack1l111ll1l1l_opy_ = bstack11l1l11_opy_ (u"ࠨࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡩࡴࡡࡶࡧࡦࡴ࡮ࡪࡰࡪࠦᐭ")
    bstack1l1111lllll_opy_ = bstack11l1l11_opy_ (u"ࠢࡥࡴ࡬ࡺࡪࡸ࡟ࡩࡣࡶࡣࡺࡸ࡬ࠣᐮ")
    scripts: Dict[str, Dict[str, str]]
    commands: Dict[str, Dict[str, Dict[str, List[str]]]]
    def __init__(self, bstack1l11ll1llll_opy_, bstack1ll1llll11l_opy_):
        super().__init__()
        self.scripts = dict()
        self.commands = dict()
        self.accessibility = False
        self.bstack1l111llll11_opy_ = False
        self.bstack1l111ll11ll_opy_ = dict()
        if not self.is_enabled():
            return
        self.bstack1l11ll11ll1_opy_ = bstack1ll1llll11l_opy_
        bstack1l11ll1llll_opy_.bstack111111l11l_opy_((bstack1llll1l1lll_opy_.bstack1llllll1111_opy_, bstack1111111l1l_opy_.PRE), self.bstack1l111l111l1_opy_)
        TestFramework.bstack111111l11l_opy_((bstack1lll1lllll1_opy_.TEST, bstack1llll1111l1_opy_.PRE), self.bstack1lll1llll1l_opy_)
        TestFramework.bstack111111l11l_opy_((bstack1lll1lllll1_opy_.TEST, bstack1llll1111l1_opy_.POST), self.bstack1lll1lll1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1llll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack11111111l1_opy_: Tuple[bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l111lll111_opy_(instance, args)
        test_framework = f.get_state(instance, TestFramework.bstack1lll1l11l1l_opy_)
        if self.bstack1l111llll11_opy_:
            self.bstack1l111ll11ll_opy_[bstack11l1l11_opy_ (u"ࠣࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠣᐯ")] = f.get_state(instance, TestFramework.bstack1llll11l1ll_opy_)
        if bstack11l1l11_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩ࠭ᐰ") in instance.bstack1ll11ll1l11_opy_:
            platform_index = f.get_state(instance, TestFramework.bstack1llll1ll111_opy_)
            self.accessibility = self.bstack1l111l1llll_opy_(tags, self.config[bstack11l1l11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ᐱ")][platform_index])
        else:
            capabilities = self.bstack1l11ll11ll1_opy_.bstack1lll1ll1lll_opy_(f, instance, bstack11111111l1_opy_, *args, **kwargs)
            if not capabilities:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠡࡨࡲࡹࡳࡪࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᐲ") + str(kwargs) + bstack11l1l11_opy_ (u"ࠧࠨᐳ"))
                return
            self.accessibility = self.bstack1l111l1llll_opy_(tags, capabilities)
        if self.bstack1l11ll11ll1_opy_.pages and self.bstack1l11ll11ll1_opy_.pages.values():
            bstack1l1111lll11_opy_ = list(self.bstack1l11ll11ll1_opy_.pages.values())
            if bstack1l1111lll11_opy_ and isinstance(bstack1l1111lll11_opy_[0], (list, tuple)) and bstack1l1111lll11_opy_[0]:
                bstack1l111lll11l_opy_ = bstack1l1111lll11_opy_[0][0]
                if callable(bstack1l111lll11l_opy_):
                    page = bstack1l111lll11l_opy_()
                    def bstack1ll1l1ll11_opy_():
                        self.get_accessibility_results(page, bstack11l1l11_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥᐴ"))
                    def bstack1l111l1l1ll_opy_():
                        self.get_accessibility_results_summary(page, bstack11l1l11_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦᐵ"))
                    setattr(page, bstack11l1l11_opy_ (u"ࠣࡩࡨࡸࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡖࡪࡹࡵ࡭ࡶࡶࠦᐶ"), bstack1ll1l1ll11_opy_)
                    setattr(page, bstack11l1l11_opy_ (u"ࠤࡪࡩࡹࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡗ࡫ࡳࡶ࡮ࡷࡗࡺࡳ࡭ࡢࡴࡼࠦᐷ"), bstack1l111l1l1ll_opy_)
        self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡷ࡭ࡵࡵ࡭ࡦࠣࡶࡺࡴࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡷࡣ࡯ࡹࡪࡃࠢᐸ") + str(self.accessibility) + bstack11l1l11_opy_ (u"ࠦࠧᐹ"))
    def bstack1l111l111l1_opy_(
        self,
        f: bstack1llllll11l1_opy_,
        driver: object,
        exec: Tuple[bstack1111111111_opy_, str],
        bstack11111111l1_opy_: Tuple[bstack1llll1l1lll_opy_, bstack1111111l1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            bstack1l11lll1l_opy_ = datetime.now()
            self.bstack1l111l1l1l1_opy_(f, exec, *args, **kwargs)
            instance, method_name = exec
            instance.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠧࡧ࠱࠲ࡻ࠽࡭ࡳ࡯ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡥࡲࡲ࡫࡯ࡧࠣᐺ"), datetime.now() - bstack1l11lll1l_opy_)
            if (
                not f.bstack1l1lll11l11_opy_(method_name)
                or f.bstack1l1lll1ll1l_opy_(method_name, *args)
                or f.bstack1l1llll1l11_opy_(method_name, *args)
            ):
                return
            if not f.get_state(instance, bstack1l1l111111l_opy_.bstack1l111l1l111_opy_, False):
                if not bstack1l1l111111l_opy_.bstack1l1ll11llll_opy_:
                    self.logger.warning(bstack11l1l11_opy_ (u"ࠨ࡛ࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸ࠾ࠤᐻ") + str(f.platform_index) + bstack11l1l11_opy_ (u"ࠢ࡞ࠢࡤ࠵࠶ࡿࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠦࡨࡢࡸࡨࠤࡳࡵࡴࠡࡤࡨࡩࡳࠦࡳࡦࡶࠣࡪࡴࡸࠠࡵࡪ࡬ࡷࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᐼ"))
                    bstack1l1l111111l_opy_.bstack1l1ll11llll_opy_ = True
                return
            bstack1l111l11l1l_opy_ = self.scripts.get(f.framework_name, {})
            if not bstack1l111l11l1l_opy_:
                platform_index = f.get_state(instance, bstack1llllll11l1_opy_.bstack1llll1ll111_opy_, 0)
                self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡰࡲࠤࡦ࠷࠱ࡺࠢࡶࡧࡷ࡯ࡰࡵࡵࠣࡪࡴࡸࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸ࠾ࡽࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࢀࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࠨᐽ") + str(f.framework_name) + bstack11l1l11_opy_ (u"ࠤࠥᐾ"))
                return
            command_name = f.bstack1l1lll11l1l_opy_(*args)
            if not command_name:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡱ࡮ࡹࡳࡪࡰࡪࠤࡨࡵ࡭࡮ࡣࡱࡨࡤࡴࡡ࡮ࡧࠣࡪࡴࡸࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࡽࡩ࠲࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࠦ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࡁࠧᐿ") + str(method_name) + bstack11l1l11_opy_ (u"ࠦࠧᑀ"))
                return
            bstack1l111lll1ll_opy_ = f.get_state(instance, bstack1l1l111111l_opy_.bstack1l1111lllll_opy_, False)
            if command_name == bstack11l1l11_opy_ (u"ࠧ࡭ࡥࡵࠤᑁ") and not bstack1l111lll1ll_opy_:
                f.bstack1llll1l1l1l_opy_(instance, bstack1l1l111111l_opy_.bstack1l1111lllll_opy_, True)
                bstack1l111lll1ll_opy_ = True
            if not bstack1l111lll1ll_opy_ and not self.bstack1l111llll11_opy_:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠨ࡮ࡰࠢࡘࡖࡑࠦ࡬ࡰࡣࡧࡩࡩࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࡼࡨ࠱ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁࠥࡩ࡯࡮࡯ࡤࡲࡩࡥ࡮ࡢ࡯ࡨࡁࠧᑂ") + str(command_name) + bstack11l1l11_opy_ (u"ࠢࠣᑃ"))
                return
            scripts_to_run = self.commands.get(f.framework_name, {}).get(method_name, {}).get(command_name, [])
            if not scripts_to_run:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡰࡲࠤࡦ࠷࠱ࡺࠢࡶࡧࡷ࡯ࡰࡵࡵࠣࡪࡴࡸࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࡽࡩ࠲࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࠦࡣࡰ࡯ࡰࡥࡳࡪ࡟࡯ࡣࡰࡩࡂࠨᑄ") + str(command_name) + bstack11l1l11_opy_ (u"ࠤࠥᑅ"))
                return
            self.logger.info(bstack11l1l11_opy_ (u"ࠥࡶࡺࡴ࡮ࡪࡰࡪࠤࢀࡲࡥ࡯ࠪࡶࡧࡷ࡯ࡰࡵࡵࡢࡸࡴࡥࡲࡶࡰࠬࢁࠥࡹࡣࡳ࡫ࡳࡸࡸࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࡼࡨ࠱ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁࠥࡩ࡯࡮࡯ࡤࡲࡩࡥ࡮ࡢ࡯ࡨࡁࠧᑆ") + str(command_name) + bstack11l1l11_opy_ (u"ࠦࠧᑇ"))
            scripts = [(s, bstack1l111l11l1l_opy_[s]) for s in scripts_to_run if s in bstack1l111l11l1l_opy_]
            for script_name, bstack1lll1llll11_opy_ in scripts:
                try:
                    bstack1l11lll1l_opy_ = datetime.now()
                    if script_name == bstack11l1l11_opy_ (u"ࠧࡹࡣࡢࡰࠥᑈ"):
                        result = self.perform_scan(driver, method=command_name, framework_name=f.framework_name)
                    instance.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠨࡡ࠲࠳ࡼ࠾ࠧᑉ") + script_name, datetime.now() - bstack1l11lll1l_opy_)
                    if isinstance(result, dict) and not result.get(bstack11l1l11_opy_ (u"ࠢࡴࡷࡦࡧࡪࡹࡳࠣᑊ"), True):
                        self.logger.warning(bstack11l1l11_opy_ (u"ࠣࡵ࡮࡭ࡵࠦࡥࡹࡧࡦࡹࡹ࡯࡮ࡨࠢࡵࡩࡲࡧࡩ࡯࡫ࡱ࡫ࠥࡹࡣࡳ࡫ࡳࡸࡸࡀࠠࠣᑋ") + str(result) + bstack11l1l11_opy_ (u"ࠤࠥᑌ"))
                        break
                except Exception as e:
                    self.logger.error(bstack11l1l11_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠢࡨࡼࡪࡩࡵࡵ࡫ࡱ࡫ࠥࡹࡣࡳ࡫ࡳࡸࡂࢁࡳࡤࡴ࡬ࡴࡹࡥ࡮ࡢ࡯ࡨࢁࠥ࡫ࡲࡳࡱࡵࡁࠧᑍ") + str(e) + bstack11l1l11_opy_ (u"ࠦࠧᑎ"))
        except Exception as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡧࡻࡩࡨࡻࡴࡦࠢࡨࡶࡷࡵࡲ࠾ࠤᑏ") + str(e) + bstack11l1l11_opy_ (u"ࠨࠢᑐ"))
    def bstack1lll1lll1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll11_opy_,
        bstack11111111l1_opy_: Tuple[bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1l111lll111_opy_(instance, args)
        capabilities = self.bstack1l11ll11ll1_opy_.bstack1lll1ll1lll_opy_(f, instance, bstack11111111l1_opy_, *args, **kwargs)
        self.accessibility = self.bstack1l111l1llll_opy_(tags, capabilities)
        if not self.accessibility:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡣ࠴࠵ࡾࠦ࡮ࡰࡶࠣࡩࡳࡧࡢ࡭ࡧࡧࠦᑑ"))
            return
        driver = self.bstack1l11ll11ll1_opy_.bstack1llll111l11_opy_(f, instance, bstack11111111l1_opy_, *args, **kwargs)
        test_name = f.get_state(instance, TestFramework.bstack1ll11111lll_opy_)
        if not test_name:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡰࡤࡱࡪࠨᑒ"))
            return
        test_uuid = f.get_state(instance, TestFramework.bstack1llll11l1ll_opy_)
        if not test_uuid:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡱ࡮ࡹࡳࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡸࡹ࡮ࡪࠢᑓ"))
            return
        if isinstance(self.bstack1l11ll11ll1_opy_, bstack1lll1ll11ll_opy_):
            framework_name = bstack11l1l11_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᑔ")
        else:
            framework_name = bstack11l1l11_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭ᑕ")
        self.bstack11l11l1l_opy_(driver, test_name, framework_name, test_uuid)
    def perform_scan(self, driver: object, method: Union[None, str], framework_name: str):
        bstack1ll11lll11l_opy_ = bstack111111111l_opy_.bstack1ll1111llll_opy_(EVENTS.bstack11ll11ll11_opy_.value)
        if not self.accessibility:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡶࡥࡳࡨࡲࡶࡲࡥࡳࡤࡣࡱ࠾ࠥࡧ࠱࠲ࡻࠣࡲࡴࡺࠠࡦࡰࡤࡦࡱ࡫ࡤࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁࠥࠨᑖ"))
            return
        bstack1l11lll1l_opy_ = datetime.now()
        bstack1lll1llll11_opy_ = self.scripts.get(framework_name, {}).get(bstack11l1l11_opy_ (u"ࠨࡳࡤࡣࡱࠦᑗ"), None)
        if not bstack1lll1llll11_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࠩࡶࡧࡦࡴࠧࠡࡵࡦࡶ࡮ࡶࡴࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࠢᑘ") + str(framework_name) + bstack11l1l11_opy_ (u"ࠣࠢࠥᑙ"))
            return
        if self.bstack1l111llll11_opy_:
            arg = dict()
            arg[bstack11l1l11_opy_ (u"ࠤࡰࡩࡹ࡮࡯ࡥࠤᑚ")] = method if method else bstack11l1l11_opy_ (u"ࠥࠦᑛ")
            arg[bstack11l1l11_opy_ (u"ࠦࡹ࡮ࡔࡦࡵࡷࡖࡺࡴࡕࡶ࡫ࡧࠦᑜ")] = self.bstack1l111ll11ll_opy_[bstack11l1l11_opy_ (u"ࠧࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠧᑝ")]
            arg[bstack11l1l11_opy_ (u"ࠨࡴࡩࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠦᑞ")] = self.bstack1l111ll11ll_opy_[bstack11l1l11_opy_ (u"ࠢࡵࡧࡶࡸ࡭ࡻࡢࡠࡤࡸ࡭ࡱࡪ࡟ࡶࡷ࡬ࡨࠧᑟ")]
            arg[bstack11l1l11_opy_ (u"ࠣࡣࡸࡸ࡭ࡎࡥࡢࡦࡨࡶࠧᑠ")] = self.bstack1l111ll11ll_opy_[bstack11l1l11_opy_ (u"ࠤࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡖࡲ࡯ࡪࡴࠢᑡ")]
            arg[bstack11l1l11_opy_ (u"ࠥࡸ࡭ࡐࡷࡵࡖࡲ࡯ࡪࡴࠢᑢ")] = self.bstack1l111ll11ll_opy_[bstack11l1l11_opy_ (u"ࠦࡹ࡮࡟࡫ࡹࡷࡣࡹࡵ࡫ࡦࡰࠥᑣ")]
            arg[bstack11l1l11_opy_ (u"ࠧࡹࡣࡢࡰࡗ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠧᑤ")] = str(int(datetime.now().timestamp() * 1000))
            bstack1l1111ll11l_opy_ = bstack1lll1llll11_opy_ % json.dumps(arg)
            driver.execute_script(bstack1l1111ll11l_opy_)
            return
        instance = bstack1lll11ll111_opy_.bstack1ll11111111_opy_(driver)
        if instance:
            if not bstack1lll11ll111_opy_.get_state(instance, bstack1l1l111111l_opy_.bstack1l111ll1l1l_opy_, False):
                bstack1lll11ll111_opy_.bstack1llll1l1l1l_opy_(instance, bstack1l1l111111l_opy_.bstack1l111ll1l1l_opy_, True)
            else:
                self.logger.info(bstack11l1l11_opy_ (u"ࠨࡰࡦࡴࡩࡳࡷࡳ࡟ࡴࡥࡤࡲ࠿ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡪࡰࠣࡴࡷࡵࡧࡳࡧࡶࡷࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࡻࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࡾࠢࡰࡩࡹ࡮࡯ࡥ࠿ࠥᑥ") + str(method) + bstack11l1l11_opy_ (u"ࠢࠣᑦ"))
                return
        self.logger.info(bstack11l1l11_opy_ (u"ࠣࡲࡨࡶ࡫ࡵࡲ࡮ࡡࡶࡧࡦࡴ࠺ࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁࠥࡳࡥࡵࡪࡲࡨࡂࠨᑧ") + str(method) + bstack11l1l11_opy_ (u"ࠤࠥᑨ"))
        if framework_name == bstack11l1l11_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᑩ"):
            result = self.bstack1l11ll11ll1_opy_.bstack1lll1l1l1l1_opy_(driver, bstack1lll1llll11_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1llll11_opy_, {bstack11l1l11_opy_ (u"ࠦࡲ࡫ࡴࡩࡱࡧࠦᑪ"): method if method else bstack11l1l11_opy_ (u"ࠧࠨᑫ")})
        bstack111111111l_opy_.end(EVENTS.bstack11ll11ll11_opy_.value, bstack1ll11lll11l_opy_+bstack11l1l11_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᑬ"), bstack1ll11lll11l_opy_+bstack11l1l11_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᑭ"), True, None, command=method)
        if instance:
            bstack1lll11ll111_opy_.bstack1llll1l1l1l_opy_(instance, bstack1l1l111111l_opy_.bstack1l111ll1l1l_opy_, False)
            instance.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠣࡣ࠴࠵ࡾࡀࡰࡦࡴࡩࡳࡷࡳ࡟ࡴࡥࡤࡲࠧᑮ"), datetime.now() - bstack1l11lll1l_opy_)
        return result
        def bstack1l1111l1ll1_opy_(self, driver: object, framework_name, bstack1lll11l11_opy_: str):
            self.bstack1llllllll11_opy_()
            req = structs.AccessibilityResultRequest()
            req.bin_session_id = self.bin_session_id
            req.bstack1l111ll1lll_opy_ = self.bstack1l111ll11ll_opy_[bstack11l1l11_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠤᑯ")]
            req.bstack1lll11l11_opy_ = bstack1lll11l11_opy_
            req.session_id = self.bin_session_id
            try:
                r = self.bstack1llll1ll11l_opy_.AccessibilityResult(req)
                if not r.success:
                    self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࠧᑰ") + str(r) + bstack11l1l11_opy_ (u"ࠦࠧᑱ"))
                else:
                    bstack1l111l1111l_opy_ = json.loads(r.bstack1l1111lll1l_opy_.decode(bstack11l1l11_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᑲ")))
                    if bstack1lll11l11_opy_ == bstack11l1l11_opy_ (u"࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࠪᑳ"):
                        return bstack1l111l1111l_opy_.get(bstack11l1l11_opy_ (u"ࠢࡥࡣࡷࡥࠧᑴ"), [])
                    else:
                        return bstack1l111l1111l_opy_.get(bstack11l1l11_opy_ (u"ࠣࡦࡤࡸࡦࠨᑵ"), {})
            except grpc.RpcError as e:
                self.logger.error(bstack11l1l11_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤ࡫࡫ࡴࡤࡪ࡬ࡲ࡬ࠦࡧࡦࡶࡢࡥࡵࡶ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡳࡧࡶࡹࡱࡺࠠࡧࡴࡲࡱࠥࡩ࡬ࡪ࠼ࠣࠦᑶ") + str(e) + bstack11l1l11_opy_ (u"ࠥࠦᑷ"))
    @measure(event_name=EVENTS.bstack1l1l111ll_opy_, stage=STAGE.bstack11l1lllll_opy_)
    def get_accessibility_results(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡴࡨࡷࡺࡲࡴࡴ࠼ࠣࡥ࠶࠷ࡹࠡࡰࡲࡸࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠨᑸ"))
            return
        if self.bstack1l111llll11_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࡦࡶࡰࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᑹ"))
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l1111l1ll1_opy_(driver, framework_name, bstack11l1l11_opy_ (u"ࠨࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࠥᑺ"))
        bstack1lll1llll11_opy_ = self.scripts.get(framework_name, {}).get(bstack11l1l11_opy_ (u"ࠢࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠦᑻ"), None)
        if not bstack1lll1llll11_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠣ࡯࡬ࡷࡸ࡯࡮ࡨࠢࠪ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠧࠡࡵࡦࡶ࡮ࡶࡴࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࠢᑼ") + str(framework_name) + bstack11l1l11_opy_ (u"ࠤࠥᑽ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1l11lll1l_opy_ = datetime.now()
        if framework_name == bstack11l1l11_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᑾ"):
            result = self.bstack1l11ll11ll1_opy_.bstack1lll1l1l1l1_opy_(driver, bstack1lll1llll11_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1llll11_opy_)
        instance = bstack1lll11ll111_opy_.bstack1ll11111111_opy_(driver)
        if instance:
            instance.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠦࡦ࠷࠱ࡺ࠼ࡪࡩࡹࡥࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡲࡦࡵࡸࡰࡹࡹࠢᑿ"), datetime.now() - bstack1l11lll1l_opy_)
        return result
    @measure(event_name=EVENTS.bstack111l1ll11l_opy_, stage=STAGE.bstack11l1lllll_opy_)
    def get_accessibility_results_summary(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡵࡩࡸࡻ࡬ࡵࡵࡢࡷࡺࡳ࡭ࡢࡴࡼ࠾ࠥࡧ࠱࠲ࡻࠣࡲࡴࡺࠠࡦࡰࡤࡦࡱ࡫ࡤࠣᒀ"))
            return
        if self.bstack1l111llll11_opy_:
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1l1111l1ll1_opy_(driver, framework_name, bstack11l1l11_opy_ (u"࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࡖࡹࡲࡳࡡࡳࡻࠪᒁ"))
        bstack1lll1llll11_opy_ = self.scripts.get(framework_name, {}).get(bstack11l1l11_opy_ (u"ࠢࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࡗࡺࡳ࡭ࡢࡴࡼࠦᒂ"), None)
        if not bstack1lll1llll11_opy_:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠣ࡯࡬ࡷࡸ࡯࡮ࡨࠢࠪ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࡓࡶ࡯ࡰࡥࡷࡿࠧࠡࡵࡦࡶ࡮ࡶࡴࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࠢᒃ") + str(framework_name) + bstack11l1l11_opy_ (u"ࠤࠥᒄ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack1l11lll1l_opy_ = datetime.now()
        if framework_name == bstack11l1l11_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᒅ"):
            result = self.bstack1l11ll11ll1_opy_.bstack1lll1l1l1l1_opy_(driver, bstack1lll1llll11_opy_)
        else:
            result = driver.execute_async_script(bstack1lll1llll11_opy_)
        instance = bstack1lll11ll111_opy_.bstack1ll11111111_opy_(driver)
        if instance:
            instance.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠦࡦ࠷࠱ࡺ࠼ࡪࡩࡹࡥࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡲࡦࡵࡸࡰࡹࡹ࡟ࡴࡷࡰࡱࡦࡸࡹࠣᒆ"), datetime.now() - bstack1l11lll1l_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l111l11lll_opy_, stage=STAGE.bstack11l1lllll_opy_)
    def bstack1l1111l1lll_opy_(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str,
    ):
        self.bstack1llllllll11_opy_()
        req = structs.AccessibilityConfigRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        try:
            r = self.bstack1llll1ll11l_opy_.AccessibilityConfig(req)
            if not r.success:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢᒇ") + str(r) + bstack11l1l11_opy_ (u"ࠨࠢᒈ"))
            else:
                self.bstack1l1111ll111_opy_(framework_name, r)
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧᒉ") + str(e) + bstack11l1l11_opy_ (u"ࠣࠤᒊ"))
            traceback.print_exc()
            raise e
    def bstack1l1111ll111_opy_(self, framework_name: str, result: structs.AccessibilityConfigResponse) -> bool:
        if not result.success or not result.accessibility.success:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠤ࡯ࡳࡦࡪ࡟ࡤࡱࡱࡪ࡮࡭࠺ࠡࡣ࠴࠵ࡾࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥࠤᒋ"))
            return False
        if result.accessibility.is_app_accessibility:
            self.bstack1l111llll11_opy_ = result.accessibility.is_app_accessibility
        if result.testhub.build_hashed_id:
            self.bstack1l111ll11ll_opy_[bstack11l1l11_opy_ (u"ࠥࡸࡪࡹࡴࡩࡷࡥࡣࡧࡻࡩ࡭ࡦࡢࡹࡺ࡯ࡤࠣᒌ")] = result.testhub.build_hashed_id
        if result.testhub.jwt:
            self.bstack1l111ll11ll_opy_[bstack11l1l11_opy_ (u"ࠦࡹ࡮࡟࡫ࡹࡷࡣࡹࡵ࡫ࡦࡰࠥᒍ")] = result.testhub.jwt
        if result.accessibility.options:
            options = result.accessibility.options
            if options.capabilities:
                for caps in options.capabilities:
                    self.bstack1l111ll11ll_opy_[caps.name] = caps.value
            if options.scripts:
                self.scripts[framework_name] = {row.name: row.command for row in options.scripts}
            if options.commands_to_wrap and options.commands_to_wrap.commands:
                scripts_to_run = [s for s in options.commands_to_wrap.scripts_to_run]
                if not scripts_to_run:
                    return False
                bstack1l111ll11l1_opy_ = dict()
                for command in options.commands_to_wrap.commands:
                    if command.library == self.bstack1l1111ll1l1_opy_ and command.module == self.bstack1l111lllll1_opy_:
                        if command.method and not command.method in bstack1l111ll11l1_opy_:
                            bstack1l111ll11l1_opy_[command.method] = dict()
                        if command.name and not command.name in bstack1l111ll11l1_opy_[command.method]:
                            bstack1l111ll11l1_opy_[command.method][command.name] = list()
                        bstack1l111ll11l1_opy_[command.method][command.name].extend(scripts_to_run)
                self.commands[framework_name] = bstack1l111ll11l1_opy_
        return bool(self.commands.get(framework_name, None))
    def bstack1l111l1l1l1_opy_(
        self,
        f: bstack1llllll11l1_opy_,
        exec: Tuple[bstack1111111111_opy_, str],
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if isinstance(self.bstack1l11ll11ll1_opy_, bstack1lll1ll11ll_opy_) and method_name != bstack11l1l11_opy_ (u"ࠬࡩ࡯࡯ࡰࡨࡧࡹ࠭ᒎ"):
            return
        if bstack1lll11ll111_opy_.bstack1111111ll1_opy_(instance, bstack1l1l111111l_opy_.bstack1l111l1l111_opy_):
            return
        if f.bstack1llll1lll1l_opy_(method_name, *args):
            bstack1l111ll1l11_opy_ = False
            desired_capabilities = f.bstack1l1lll11lll_opy_(instance)
            if isinstance(desired_capabilities, dict):
                hub_url = f.bstack1l1lll1lll1_opy_(instance)
                platform_index = f.get_state(instance, bstack1llllll11l1_opy_.bstack1llll1ll111_opy_, 0)
                bstack1l111l1ll1l_opy_ = datetime.now()
                r = self.bstack1l1111l1lll_opy_(platform_index, f.framework_name, f.framework_version, hub_url)
                instance.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡨࡵ࡮ࡧ࡫ࡪࠦᒏ"), datetime.now() - bstack1l111l1ll1l_opy_)
                bstack1l111ll1l11_opy_ = r.success
            else:
                self.logger.error(bstack11l1l11_opy_ (u"ࠢ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡦࡨࡷ࡮ࡸࡥࡥࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳ࠾ࠤᒐ") + str(desired_capabilities) + bstack11l1l11_opy_ (u"ࠣࠤᒑ"))
            f.bstack1llll1l1l1l_opy_(instance, bstack1l1l111111l_opy_.bstack1l111l1l111_opy_, bstack1l111ll1l11_opy_)
    def bstack111111l1l_opy_(self, test_tags):
        bstack1l1111l1lll_opy_ = self.config.get(bstack11l1l11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᒒ"))
        if not bstack1l1111l1lll_opy_:
            return True
        try:
            include_tags = bstack1l1111l1lll_opy_[bstack11l1l11_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨᒓ")] if bstack11l1l11_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩᒔ") in bstack1l1111l1lll_opy_ and isinstance(bstack1l1111l1lll_opy_[bstack11l1l11_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪᒕ")], list) else []
            exclude_tags = bstack1l1111l1lll_opy_[bstack11l1l11_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫᒖ")] if bstack11l1l11_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬᒗ") in bstack1l1111l1lll_opy_ and isinstance(bstack1l1111l1lll_opy_[bstack11l1l11_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ᒘ")], list) else []
            excluded = any(tag in exclude_tags for tag in test_tags)
            included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
            return not excluded and included
        except Exception as error:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡷࡣ࡯࡭ࡩࡧࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡧࡱࡵࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡧ࡫ࡦࡰࡴࡨࠤࡸࡩࡡ࡯ࡰ࡬ࡲ࡬࠴ࠠࡆࡴࡵࡳࡷࠦ࠺ࠡࠤᒙ") + str(error))
        return False
    def bstack1ll1ll1l1_opy_(self, caps):
        try:
            if self.bstack1l111llll11_opy_:
                bstack1l111llll1l_opy_ = caps.get(bstack11l1l11_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠤᒚ"))
                if bstack1l111llll1l_opy_ is not None and str(bstack1l111llll1l_opy_).lower() == bstack11l1l11_opy_ (u"ࠦࡦࡴࡤࡳࡱ࡬ࡨࠧᒛ"):
                    bstack1l111l11l11_opy_ = caps.get(bstack11l1l11_opy_ (u"ࠧࡧࡰࡱ࡫ࡸࡱ࠿ࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢᒜ")) or caps.get(bstack11l1l11_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣᒝ"))
                    if bstack1l111l11l11_opy_ is not None and int(bstack1l111l11l11_opy_) < 11:
                        self.logger.warning(bstack11l1l11_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡂࡰࡧࡶࡴ࡯ࡤࠡ࠳࠴ࠤࡦࡴࡤࠡࡣࡥࡳࡻ࡫࠮ࠡࡅࡸࡶࡷ࡫࡮ࡵࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥࡃࠢᒞ") + str(bstack1l111l11l11_opy_) + bstack11l1l11_opy_ (u"ࠣࠤᒟ"))
                        return False
                return True
            bstack1l111l111ll_opy_ = caps.get(bstack11l1l11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᒠ"), {}).get(bstack11l1l11_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧᒡ"), caps.get(bstack11l1l11_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫᒢ"), bstack11l1l11_opy_ (u"ࠬ࠭ᒣ")))
            if bstack1l111l111ll_opy_:
                self.logger.warning(bstack11l1l11_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡄࡦࡵ࡮ࡸࡴࡶࠠࡣࡴࡲࡻࡸ࡫ࡲࡴ࠰ࠥᒤ"))
                return False
            browser = caps.get(bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬᒥ"), bstack11l1l11_opy_ (u"ࠨࠩᒦ")).lower()
            if browser != bstack11l1l11_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩᒧ"):
                self.logger.warning(bstack11l1l11_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨᒨ"))
                return False
            bstack1l111l11ll1_opy_ = bstack1l111l1lll1_opy_
            if not self.config.get(bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᒩ")) or self.config.get(bstack11l1l11_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩᒪ")):
                bstack1l111l11ll1_opy_ = bstack1l1111ll1ll_opy_
            browser_version = caps.get(bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᒫ"))
            if not browser_version:
                browser_version = caps.get(bstack11l1l11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᒬ"), {}).get(bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᒭ"), bstack11l1l11_opy_ (u"ࠩࠪᒮ"))
            if browser_version and browser_version != bstack11l1l11_opy_ (u"ࠪࡰࡦࡺࡥࡴࡶࠪᒯ") and int(browser_version.split(bstack11l1l11_opy_ (u"ࠫ࠳࠭ᒰ"))[0]) <= bstack1l111l11ll1_opy_:
                self.logger.warning(bstack11l1l11_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡉࡨࡳࡱࡰࡩࠥࡨࡲࡰࡹࡶࡩࡷࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡨࡴࡨࡥࡹ࡫ࡲࠡࡶ࡫ࡥࡳࠦࠢᒱ") + str(bstack1l111l11ll1_opy_) + bstack11l1l11_opy_ (u"ࠨ࠮ࠣᒲ"))
                return False
            bstack1l111ll1ll1_opy_ = caps.get(bstack11l1l11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᒳ"), {}).get(bstack11l1l11_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᒴ"))
            if not bstack1l111ll1ll1_opy_:
                bstack1l111ll1ll1_opy_ = caps.get(bstack11l1l11_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧᒵ"), {})
            if bstack1l111ll1ll1_opy_ and bstack11l1l11_opy_ (u"ࠪ࠱࠲࡮ࡥࡢࡦ࡯ࡩࡸࡹࠧᒶ") in bstack1l111ll1ll1_opy_.get(bstack11l1l11_opy_ (u"ࠫࡦࡸࡧࡴࠩᒷ"), []):
                self.logger.warning(bstack11l1l11_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠ࡯ࡱࡷࠤࡷࡻ࡮ࠡࡱࡱࠤࡱ࡫ࡧࡢࡥࡼࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲࡙ࠥࡷࡪࡶࡦ࡬ࠥࡺ࡯ࠡࡰࡨࡻࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩࠥࡵࡲࠡࡣࡹࡳ࡮ࡪࠠࡶࡵ࡬ࡲ࡬ࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪ࠴ࠢᒸ"))
                return False
            return True
        except Exception as error:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡼࡡ࡭࡫ࡧࡥࡹ࡫ࠠࡢ࠳࠴ࡽࠥࡹࡵࡱࡲࡲࡶࡹࠦ࠺ࠣᒹ") + str(error))
            return False
    def bstack1l111l1l11l_opy_(self, test_uuid: str, result: structs.FetchDriverExecuteParamsEventResponse):
        bstack1l111lll1l1_opy_ = {
            bstack11l1l11_opy_ (u"ࠧࡵࡪࡗࡩࡸࡺࡒࡶࡰࡘࡹ࡮ࡪࠧᒺ"): test_uuid,
        }
        bstack1l111l1ll11_opy_ = {}
        if result.success:
            bstack1l111l1ll11_opy_ = json.loads(result.accessibility_execute_params)
        return bstack1l1111llll1_opy_(bstack1l111lll1l1_opy_, bstack1l111l1ll11_opy_)
    def bstack11l11l1l_opy_(self, driver: object, name: str, framework_name: str, test_uuid: str):
        bstack1ll11lll11l_opy_ = None
        try:
            self.bstack1llllllll11_opy_()
            req = structs.FetchDriverExecuteParamsEventRequest()
            req.bin_session_id = self.bin_session_id
            req.product = bstack11l1l11_opy_ (u"ࠣࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠣᒻ")
            req.script_name = bstack11l1l11_opy_ (u"ࠤࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠢᒼ")
            r = self.bstack1llll1ll11l_opy_.FetchDriverExecuteParamsEvent(req)
            if not r.success:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥࡪࡲࡪࡸࡨࡶࠥ࡫ࡸࡦࡥࡸࡸࡪࠦࡰࡢࡴࡤࡱࡸࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨᒽ") + str(r.error) + bstack11l1l11_opy_ (u"ࠦࠧᒾ"))
            else:
                bstack1l111lll1l1_opy_ = self.bstack1l111l1l11l_opy_(test_uuid, r)
                bstack1lll1llll11_opy_ = r.script
            self.logger.debug(bstack11l1l11_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡣࡹ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠨᒿ") + str(bstack1l111lll1l1_opy_))
            self.perform_scan(driver, name, framework_name=framework_name)
            if not bstack1lll1llll11_opy_:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡰࡦࡴࡩࡳࡷࡳ࡟ࡴࡥࡤࡲ࠿ࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࠨࡵࡤࡺࡪࡘࡥࡴࡷ࡯ࡸࡸ࠭ࠠࡴࡥࡵ࡭ࡵࡺࠠࡧࡱࡵࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࠨᓀ") + str(framework_name) + bstack11l1l11_opy_ (u"ࠢࠡࠤᓁ"))
                return
            bstack1ll11lll11l_opy_ = bstack111111111l_opy_.bstack1ll1111llll_opy_(EVENTS.bstack1l111ll111l_opy_.value)
            self.bstack1l111l11111_opy_(driver, bstack1lll1llll11_opy_, bstack1l111lll1l1_opy_, framework_name)
            self.logger.info(bstack11l1l11_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢࡩࡳࡷࠦࡴࡩ࡫ࡶࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡩࡣࡶࠤࡪࡴࡤࡦࡦ࠱ࠦᓂ"))
            bstack111111111l_opy_.end(EVENTS.bstack1l111ll111l_opy_.value, bstack1ll11lll11l_opy_+bstack11l1l11_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᓃ"), bstack1ll11lll11l_opy_+bstack11l1l11_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᓄ"), True, None, command=bstack11l1l11_opy_ (u"ࠫࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠩᓅ"),test_name=name)
        except Exception as bstack1l111ll1111_opy_:
            self.logger.error(bstack11l1l11_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸࠦࡣࡰࡷ࡯ࡨࠥࡴ࡯ࡵࠢࡥࡩࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡤࠡࡨࡲࡶࠥࡺࡨࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩ࠿ࠦࠢᓆ") + bstack11l1l11_opy_ (u"ࠨࡳࡵࡴࠫࡴࡦࡺࡨࠪࠤᓇ") + bstack11l1l11_opy_ (u"ࠢࠡࡇࡵࡶࡴࡸࠠ࠻ࠤᓈ") + str(bstack1l111ll1111_opy_))
            bstack111111111l_opy_.end(EVENTS.bstack1l111ll111l_opy_.value, bstack1ll11lll11l_opy_+bstack11l1l11_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᓉ"), bstack1ll11lll11l_opy_+bstack11l1l11_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᓊ"), False, bstack1l111ll1111_opy_, command=bstack11l1l11_opy_ (u"ࠪࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠨᓋ"),test_name=name)
    def bstack1l111l11111_opy_(self, driver, bstack1lll1llll11_opy_, bstack1l111lll1l1_opy_, framework_name):
        if framework_name == bstack11l1l11_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᓌ"):
            self.bstack1l11ll11ll1_opy_.bstack1lll1l1l1l1_opy_(driver, bstack1lll1llll11_opy_, bstack1l111lll1l1_opy_)
        else:
            self.logger.debug(driver.execute_async_script(bstack1lll1llll11_opy_, bstack1l111lll1l1_opy_))
    def _1l111lll111_opy_(self, instance: bstack1lll1l1ll11_opy_, args: Tuple) -> list:
        bstack11l1l11_opy_ (u"ࠧࠨࠢࡆࡺࡷࡶࡦࡩࡴࠡࡶࡤ࡫ࡸࠦࡢࡢࡵࡨࡨࠥࡵ࡮ࠡࡶ࡫ࡩࠥࡺࡥࡴࡶࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠴ࠢࠣࠤᓍ")
        if bstack11l1l11_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠪᓎ") in instance.bstack1ll11ll1l11_opy_:
            return args[2].tags if hasattr(args[2], bstack11l1l11_opy_ (u"ࠧࡵࡣࡪࡷࠬᓏ")) else []
        if hasattr(args[0], bstack11l1l11_opy_ (u"ࠨࡱࡺࡲࡤࡳࡡࡳ࡭ࡨࡶࡸ࠭ᓐ")):
            return [marker.name for marker in args[0].own_markers]
        return []
    def bstack1l111l1llll_opy_(self, tags, capabilities):
        return self.bstack111111l1l_opy_(tags) and self.bstack1ll1ll1l1_opy_(capabilities)