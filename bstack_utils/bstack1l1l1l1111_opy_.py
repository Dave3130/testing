# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l1l11ll1l_opy_, bstack11l11lll1ll_opy_, bstack11l11ll1l1l_opy_
import tempfile
import json
bstack11111lll111_opy_ = os.getenv(bstack1ll11_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡍ࡟ࡇࡋࡏࡉࠧẤ"), None) or os.path.join(tempfile.gettempdir(), bstack1ll11_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡩ࡫ࡢࡶࡩ࠱ࡰࡴ࡭ࠢấ"))
bstack11111ll1l11_opy_ = os.path.join(bstack1ll11_opy_ (u"ࠨ࡬ࡰࡩࠥẦ"), bstack1ll11_opy_ (u"ࠧࡴࡦ࡮࠱ࡨࡲࡩ࠮ࡦࡨࡦࡺ࡭࠮࡭ࡱࡪࠫầ"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack1ll11_opy_ (u"ࠨࠧࠫࡥࡸࡩࡴࡪ࡯ࡨ࠭ࡸ࡛ࠦࠦࠪࡱࡥࡲ࡫ࠩࡴ࡟࡞ࠩ࠭ࡲࡥࡷࡧ࡯ࡲࡦࡳࡥࠪࡵࡠࠤ࠲ࠦࠥࠩ࡯ࡨࡷࡸࡧࡧࡦࠫࡶࠫẨ"),
      datefmt=bstack1ll11_opy_ (u"ࠩࠨ࡝࠲ࠫ࡭࠮ࠧࡧࡘࠪࡎ࠺ࠦࡏ࠽ࠩࡘࡠࠧẩ"),
      stream=sys.stdout
    )
  return logger
def bstack1l1l1111l1l_opy_():
  bstack1111l11111l_opy_ = os.environ.get(bstack1ll11_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡇࡉࡇ࡛ࡇࠣẪ"), bstack1ll11_opy_ (u"ࠦ࡫ࡧ࡬ࡴࡧࠥẫ"))
  return logging.DEBUG if bstack1111l11111l_opy_.lower() == bstack1ll11_opy_ (u"ࠧࡺࡲࡶࡧࠥẬ") else logging.INFO
def bstack1ll111l1111_opy_():
  global bstack11111lll111_opy_
  if os.path.exists(bstack11111lll111_opy_):
    os.remove(bstack11111lll111_opy_)
  if os.path.exists(bstack11111ll1l11_opy_):
    os.remove(bstack11111ll1l11_opy_)
def bstack111llllll1_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def configure_logger(config, log_level):
  bstack11111l1llll_opy_ = log_level
  if bstack1ll11_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨậ") in config and config[bstack1ll11_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩẮ")] in bstack11l11lll1ll_opy_:
    bstack11111l1llll_opy_ = bstack11l11lll1ll_opy_[config[bstack1ll11_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪắ")]]
  if config.get(bstack1ll11_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫẰ"), False):
    logging.getLogger().setLevel(bstack11111l1llll_opy_)
    return bstack11111l1llll_opy_
  global bstack11111lll111_opy_
  bstack111llllll1_opy_()
  bstack11111ll111l_opy_ = logging.Formatter(
    fmt=bstack1ll11_opy_ (u"ࠪࠩ࠭ࡧࡳࡤࡶ࡬ࡱࡪ࠯ࡳࠡ࡝ࠨࠬࡳࡧ࡭ࡦࠫࡶࡡࡠࠫࠨ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠬࡷࡢࠦ࠭ࠡࠧࠫࡱࡪࡹࡳࡢࡩࡨ࠭ࡸ࠭ằ"),
    datefmt=bstack1ll11_opy_ (u"ࠫࠪ࡟࠭ࠦ࡯࠰ࠩࡩ࡚ࠥࡉ࠼ࠨࡑ࠿ࠫࡓ࡛ࠩẲ"),
  )
  bstack11111ll1lll_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack11111lll111_opy_)
  file_handler.setFormatter(bstack11111ll111l_opy_)
  bstack11111ll1lll_opy_.setFormatter(bstack11111ll111l_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack11111ll1lll_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack1ll11_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠮ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴ࠱ࡶࡪࡳ࡯ࡵࡧ࠱ࡶࡪࡳ࡯ࡵࡧࡢࡧࡴࡴ࡮ࡦࡥࡷ࡭ࡴࡴࠧẳ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack11111ll1lll_opy_.setLevel(bstack11111l1llll_opy_)
  logging.getLogger().addHandler(bstack11111ll1lll_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack11111l1llll_opy_
def bstack11111l1lll1_opy_(config):
  try:
    bstack11111l1ll1l_opy_ = set(bstack11l11ll1l1l_opy_)
    bstack11111llll1l_opy_ = bstack1ll11_opy_ (u"࠭ࠧẴ")
    with open(bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠪẵ")) as bstack11111lll1ll_opy_:
      bstack11111llll11_opy_ = bstack11111lll1ll_opy_.read()
      bstack11111llll1l_opy_ = re.sub(bstack1ll11_opy_ (u"ࡳࠩࡡࠬࡡࡹࠫࠪࡁࠦ࠲࠯ࠪ࡜࡯ࠩẶ"), bstack1ll11_opy_ (u"ࠩࠪặ"), bstack11111llll11_opy_, flags=re.M)
      bstack11111llll1l_opy_ = re.sub(
        bstack1ll11_opy_ (u"ࡵࠫࡣ࠮࡜ࡴ࠭ࠬࡃ࠭࠭Ẹ") + bstack1ll11_opy_ (u"ࠫࢁ࠭ẹ").join(bstack11111l1ll1l_opy_) + bstack1ll11_opy_ (u"ࠬ࠯࠮ࠫࠦࠪẺ"),
        bstack1ll11_opy_ (u"ࡸࠧ࡝࠴࠽ࠤࡠࡘࡅࡅࡃࡆࡘࡊࡊ࡝ࠨẻ"),
        bstack11111llll1l_opy_, flags=re.M | re.I
      )
    def bstack11111ll11ll_opy_(dic):
      bstack11111lll1l1_opy_ = {}
      for key, value in dic.items():
        if key in bstack11111l1ll1l_opy_:
          bstack11111lll1l1_opy_[key] = bstack1ll11_opy_ (u"ࠧ࡜ࡔࡈࡈࡆࡉࡔࡆࡆࡠࠫẼ")
        else:
          if isinstance(value, dict):
            bstack11111lll1l1_opy_[key] = bstack11111ll11ll_opy_(value)
          else:
            bstack11111lll1l1_opy_[key] = value
      return bstack11111lll1l1_opy_
    bstack11111lll1l1_opy_ = bstack11111ll11ll_opy_(config)
    return {
      bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠫẽ"): bstack11111llll1l_opy_,
      bstack1ll11_opy_ (u"ࠩࡩ࡭ࡳࡧ࡬ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬẾ"): json.dumps(bstack11111lll1l1_opy_)
    }
  except Exception as e:
    return {}
def bstack11111llllll_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack1ll11_opy_ (u"ࠪࡰࡴ࡭ࠧế"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack11111ll1l1l_opy_ = os.path.join(log_dir, bstack1ll11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡨࡵ࡮ࡧ࡫ࡪࡷࠬỀ"))
  if not os.path.exists(bstack11111ll1l1l_opy_):
    bstack11111ll1ll1_opy_ = {
      bstack1ll11_opy_ (u"ࠧ࡯࡮ࡪࡲࡤࡸ࡭ࠨề"): str(inipath),
      bstack1ll11_opy_ (u"ࠨࡲࡰࡱࡷࡴࡦࡺࡨࠣỂ"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack1ll11_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡤࡱࡱࡪ࡮࡭ࡳ࠯࡬ࡶࡳࡳ࠭ể")), bstack1ll11_opy_ (u"ࠨࡹࠪỄ")) as bstack11111lll11l_opy_:
      bstack11111lll11l_opy_.write(json.dumps(bstack11111ll1ll1_opy_))
def bstack11111lllll1_opy_():
  try:
    bstack11111ll1l1l_opy_ = os.path.join(os.getcwd(), bstack1ll11_opy_ (u"ࠩ࡯ࡳ࡬࠭ễ"), bstack1ll11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡧࡴࡴࡦࡪࡩࡶ࠲࡯ࡹ࡯࡯ࠩỆ"))
    if os.path.exists(bstack11111ll1l1l_opy_):
      with open(bstack11111ll1l1l_opy_, bstack1ll11_opy_ (u"ࠫࡷ࠭ệ")) as bstack11111lll11l_opy_:
        bstack11111ll1111_opy_ = json.load(bstack11111lll11l_opy_)
      return bstack11111ll1111_opy_.get(bstack1ll11_opy_ (u"ࠬ࡯࡮ࡪࡲࡤࡸ࡭࠭Ỉ"), bstack1ll11_opy_ (u"࠭ࠧỉ")), bstack11111ll1111_opy_.get(bstack1ll11_opy_ (u"ࠧࡳࡱࡲࡸࡵࡧࡴࡩࠩỊ"), bstack1ll11_opy_ (u"ࠨࠩị"))
  except:
    pass
  return None, None
def bstack1111l1111l1_opy_():
  try:
    bstack11111ll1l1l_opy_ = os.path.join(os.getcwd(), bstack1ll11_opy_ (u"ࠩ࡯ࡳ࡬࠭Ọ"), bstack1ll11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡧࡴࡴࡦࡪࡩࡶ࠲࡯ࡹ࡯࡯ࠩọ"))
    if os.path.exists(bstack11111ll1l1l_opy_):
      os.remove(bstack11111ll1l1l_opy_)
  except:
    pass
def bstack1lllll11_opy_(config):
  try:
    from bstack_utils.helper import bstack1111ll11_opy_, bstack11l11111l_opy_
    from browserstack_sdk.sdk_cli.cli import cli
    global bstack11111lll111_opy_
    if config.get(bstack1ll11_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡻࡴࡰࡅࡤࡴࡹࡻࡲࡦࡎࡲ࡫ࡸ࠭Ỏ"), False):
      return
    uuid = os.getenv(bstack1ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪỏ")) if os.getenv(bstack1ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫỐ")) else bstack1111ll11_opy_.get_property(bstack1ll11_opy_ (u"ࠢࡴࡦ࡮ࡖࡺࡴࡉࡥࠤố"))
    if not uuid or uuid == bstack1ll11_opy_ (u"ࠨࡰࡸࡰࡱ࠭Ồ"):
      return
    bstack11111l1ll11_opy_ = [bstack1ll11_opy_ (u"ࠩࡵࡩࡶࡻࡩࡳࡧࡰࡩࡳࡺࡳ࠯ࡶࡻࡸࠬồ"), bstack1ll11_opy_ (u"ࠪࡔ࡮ࡶࡦࡪ࡮ࡨࠫỔ"), bstack1ll11_opy_ (u"ࠫࡵࡿࡰࡳࡱ࡭ࡩࡨࡺ࠮ࡵࡱࡰࡰࠬổ"), bstack11111lll111_opy_, bstack11111ll1l11_opy_]
    bstack1111l1111ll_opy_, root_path = bstack11111lllll1_opy_()
    if bstack1111l1111ll_opy_ != None:
      bstack11111l1ll11_opy_.append(bstack1111l1111ll_opy_)
    if root_path != None:
      bstack11111l1ll11_opy_.append(os.path.join(root_path, bstack1ll11_opy_ (u"ࠬࡩ࡯࡯ࡨࡷࡩࡸࡺ࠮ࡱࡻࠪỖ")))
    bstack111llllll1_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack1ll11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࠳࡬ࡰࡩࡶ࠱ࠬỗ") + uuid + bstack1ll11_opy_ (u"ࠧ࠯ࡶࡤࡶ࠳࡭ࡺࠨỘ"))
    with tarfile.open(output_file, bstack1ll11_opy_ (u"ࠣࡹ࠽࡫ࡿࠨộ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack11111l1ll11_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack11111l1lll1_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11111ll11l1_opy_ = data.encode()
        tarinfo.size = len(bstack11111ll11l1_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11111ll11l1_opy_))
    multipart_data = MultipartEncoder(
      fields= {
        bstack1ll11_opy_ (u"ࠩࡧࡥࡹࡧࠧỚ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack1ll11_opy_ (u"ࠪࡶࡧ࠭ớ")), bstack1ll11_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱ࡻ࠱࡬ࢀࡩࡱࠩỜ")),
        bstack1ll11_opy_ (u"ࠬࡩ࡬ࡪࡧࡱࡸࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧờ"): uuid
      }
    )
    bstack1111l111111_opy_ = bstack11l11111l_opy_(cli.config, [bstack1ll11_opy_ (u"ࠨࡡࡱ࡫ࡶࠦỞ"), bstack1ll11_opy_ (u"ࠢࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠢở"), bstack1ll11_opy_ (u"ࠣࡷࡳࡰࡴࡧࡤࠣỠ")], bstack11l1l11ll1l_opy_)
    response = requests.post(
      bstack1ll11_opy_ (u"ࠤࡾࢁ࠴ࡩ࡬ࡪࡧࡱࡸ࠲ࡲ࡯ࡨࡵ࠲ࡹࡵࡲ࡯ࡢࡦࠥỡ").format(bstack1111l111111_opy_),
      data=multipart_data,
      headers={bstack1ll11_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩỢ"): multipart_data.content_type},
      auth=(config[bstack1ll11_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ợ")], config[bstack1ll11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨỤ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack1ll11_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡻࡰ࡭ࡱࡤࡨࠥࡲ࡯ࡨࡵ࠽ࠤࠬụ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack1ll11_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡦࡰࡧ࡭ࡳ࡭ࠠ࡭ࡱࡪࡷ࠿࠭Ủ") + str(e))
  finally:
    try:
      bstack1ll111l1111_opy_()
      bstack1111l1111l1_opy_()
    except:
      pass